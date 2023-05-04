<script lang="ts">
    export let message : Message;

    interface Message {
        from: "bot" | "user";
        body: string;
        on: number;
    }

    let isFromUser = message.from == "user";
</script>

<div class="container">
    <div class="{isFromUser ? 'message user' : 'message'}">
        {message.body}
    </div>
</div>

<style>
    .container{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 10px;
    }
    .message{
        width: 50%;
        border-radius: 20px;
        background-color: #19192B;
        padding: 16px;
    }

    .user{
        align-self: flex-end;
        background-color: #4D38A2;
    }
</style>