<script lang="ts">
    import { ChatbubbleEllipsesOutline } from "svelte-ionicons";
</script>

<div class="header">
    <div class="first">
        <ChatbubbleEllipsesOutline size="40" />
        &nbsp; &nbsp; &nbsp;
        <div>Chitti</div>
    </div>
    <div class="last">
        <div class="img"></div>
    </div>
</div>

<style>
    .header {
        padding-left: 20px;
        padding-right: 20px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        border-bottom: 0.5px solid rgb(64, 62, 62);
        width: 100%;
        height: 100px;
    }
    .header .first {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .header .first {
        font-weight: 600;
        font-size: larger;
    }
    .img {
        border-radius: 50%;
        height: 50px;
        width: 50px;
        background-size: cover;
        background-image: url('https://images.unsplash.com/photo-1457449940276-e8deed18bfff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8cHJvZmlsZXxlbnwwfHwwfHw%3D&w=1000&q=80');
        background-repeat: no-repeat;
    }
</style>
