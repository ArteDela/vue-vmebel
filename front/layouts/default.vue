<template>
	<div>
		<Header />
		<div class="main">
			<div class="container">
				<Nuxt />
			</div>
		</div>
		<Footer />
		<div class="overlay _overlay"></div>
	</div>
</template>
<script>
	import Header from '@/components/Header';
	import Footer from '@/components/Footer';
	export default
	{
		components: { Header, Footer },
	}
</script>
<style>
*{
	outline: 0px;
	-webkit-font-smoothing: grayscale;
	-moz-osx-font-smoothing: grayscale;
}
html{font-family: 'Roboto';}
a{color:#6C6C6C;}
body
{
	margin: 0;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	height: 100vh;
	font-family: 'Roboto';
}
.main{flex: 1 0 auto;}
.overlay
{
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background: rgb(196, 196, 196);
	z-index: 4;
	transition: 0.2s;
	visibility: hidden;
	opacity: 0;
}
.overlay.show
{
	transition: .2s;
	visibility: visible;
	opacity: .38;
}
.container
{
	max-width: 1200px;
	min-width: 375px;
	width: 100%;
	margin-right: auto;
	margin-left: auto;
	position: relative;
	padding:0 20px;
	box-sizing: border-box;
}
</style>
