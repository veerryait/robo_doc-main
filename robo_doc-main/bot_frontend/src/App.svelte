<script lang="ts">
	import Chat from "./components/chat.svelte";
	import Header from "./components/header.svelte";
	import MenuBar from "./components/menu_bar.svelte";

	const load = () => {
		const main = document.querySelector<HTMLDivElement>(
			"main[data-selector = 'main']"
		)!;
		main.style.filter = "blur(0px)";
	};
</script>

<svelte:window on:load={load} />

<main data-selector="main">
	<div class="row">
		<MenuBar />
		<div class="column">
			<Header />
			<Chat />
		</div>
	</div>
</main>

<style>
	main {
		filter: blur(50px);
		transition: filter 750ms;
	}
	.row {
		display: flex;
		flex-direction: row;
	}
	.column {
		display: flex;
		flex-direction: column;
		width: 92vw;
	}
</style>
