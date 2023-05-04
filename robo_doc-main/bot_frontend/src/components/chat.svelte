<script lang="ts">
    import { Send } from "svelte-ionicons";
    import io from "socket.io-client";
    import Message from "./message.svelte";

    interface Message {
        from: "bot" | "user";
        body: string;
        on: number;
    }

    var socket = io("/test");
    socket.on("connect", function () {
        console.log("connected");
    });

    const sendMessage = () => {
        const input = document.querySelector("input");
        const data = input.value;
        socket.emit("user_input", {
            data: data,
        });
        input.value = null;
        addToMessages({
            body: data,
            from: "user",
            on: Date.now(),
        });
        return false;
    };

    socket.on("bot_response", function (data) {
        setTimeout(() => {
            addToMessages({
                body: data.response,
                from: "bot",
                on: Date.now(),
            });
        }, Math.floor(Math.random() * 2000) + 1000);
    });

    let messages: Array<Message> = [];

    const addRandomMessage = () => {
        addToMessages({
            body: "random text",
            from: Math.random() > 0.5 ? "bot" : "user",
            on: Date.now(),
        });
    };

    const addToMessages = (msg: Message) => {
        messages.push(msg);
        messages = messages;
        setTimeout(() => {
            var objDiv = document.querySelector(
                "div[data-selector='messages']"
            );
            objDiv.scrollTop = objDiv.scrollHeight;
        }, 100);
    };
</script>

<div class="chat">
    <div class="welcome-message">
        <div class="headline">Welcome to the killer robot ai</div>
        <p style="font-size: 15px;">
            I can help you find your disease and doctors nearby, or will i 😈
        </p>
    </div>
    <div class="container">
        <div class="messages" data-selector="messages">
            {#each messages as msg}
                <Message message={msg} />
            {/each}
        </div>
        <div class="text-box">
            <input
                type="text"
                placeholder="Write your deathwish..."
                on:keydown={(e) => (e.key == "Enter" ? sendMessage() : null)}
            />
            &nbsp; &nbsp; &nbsp; &nbsp;
            <div on:click={sendMessage}><Send /></div>
        </div>
    </div>
</div>

<style>
    .messages {
        overflow-y: scroll !important;
        overflow-x: hidden;
        width: 92vw;
        height: 70vh;
        scroll-behavior: smooth;
    }
    .welcome-message {
        padding: 20px;
        background: linear-gradient(90deg, #121928, rgba(0, 212, 255, 0) 100%);
    }
    .headline {
        color: #2f6397;
        font-size: 20px;
    }

    .text-box {
        padding-left: 16px;
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        user-select: none;
    }

    input {
        background-color: transparent;
        outline: none;
        border: 0.1px solid grey;
        border-radius: 8px;
        padding: 10px 16px;
        width: 100%;
        color: white;
        font-size: 18px;
    }
</style>
