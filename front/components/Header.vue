<template>
	<header>
		<div class="container">
			<div class="header__first-line">
				<button class="header__burger" @click="showCatalog">
					<svg-icon name="Burger" width="24" height="24"></svg-icon>
				</button>
				<MobileMenu
					:class="{active: isVisible}"
					v-click-outside="closeCatalog"
					@close = "closeCatalog"
				/>
				<div class="header__logo">
					<a href="/">
						<svg-icon name="Logo"  width="98" height="32"></svg-icon>
						<span class="header__logo-text">Вся мебель в одном месте</span>
					</a>
				</div>
				<div class="header_buttons">
					<button class="header_search" >
						<svg-icon name="Loupe" width="24" height="24"></svg-icon>
					</button>
					<button class="header_bookmark">
						<svg-icon name="BookMark" width="24" height="24"></svg-icon>
					</button>
				</div>
			</div>
			<div class="header__desctop-first-line">
				<div class="header__desc-logo">
					<a href="/">
						<svg-icon name="Logo" width="98" height="32"></svg-icon>
						<span class="header__logo-text">Вся мебель в одном месте</span>
					</a>
				</div>
				<div class="header__phone">
					<a href="tel:121212">8 (800) 600-08-88</a>
					<span>Республика Северная Осетия — Алания</span>
				</div>
				<nav class="header__menu-small">
					<ul>
						<li><a href="/shops/">Магазины</a></li>
						<li><a href="/about/">О компании</a></li>
						<li><a href="/contacts/">Контакты</a></li>
					</ul>
				</nav>
			</div>
			<div class="header__second-line">
				<button
					class="header__catalog"
					v-bind:class="{'header__catalog--opened':openCatalogMenu}"
					@click="toggleCatalogMenu()"
				>
					<svg-icon name="Close" class="header__catalog__close" width="16" height="16"></svg-icon>
					<svg-icon name="Burger-white" class="header__catalog__burger" width="24" height="24"></svg-icon>
					Каталог
				</button>
				<div class="header__search-input">
					<input type="text" placeholder="Поиск">
					<button>
						<svg-icon name="Loupe" width="24" height="24"></svg-icon>
					</button>
				</div>
				<div class="header__big-buttons">
					<a href="#">
						<svg-icon name="Man" width="24" height="24"></svg-icon>
						Войти
					</a>
					<NuxtLink to="/favorites/">
						<svg-icon name="BookMark" width="24" height="24"></svg-icon>
						Избранное
					</NuxtLink>
				</div>
			</div>
		</div>
		<CatalogPopup v-if="openCatalogMenu"></CatalogPopup>
	</header>
</template>
<script>
	import MobileMenu from '@/components/MobileMenu'
	import CatalogPopup from '@/components/CatalogPopup'
	export default
	{
		data()
		{
			return {
				isVisible:false,
				openCatalogMenu:false
			};
		},
		components: { MobileMenu, CatalogPopup},
		methods:
		{
			toggleCatalogMenu()
			{
				this.openCatalogMenu = !this.openCatalogMenu;
			},
			showCatalog()
			{
				setTimeout(()=>{
					this.isVisible = true;
					document.querySelector('._overlay').classList.add('show')
				},0)
			},
			closeCatalog()
			{
				if(this.isVisible)
					this.isVisible = false;
				document.querySelector('._overlay').classList.remove('show')
			}
		},
		mounted()
		{
		}
	}
</script>
<style lang="scss">
	.header{flex: 0 0 auto;}
	header .container{padding-top: 20px;}
	.header__first-line
	{
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.header__burger
	{
		background: none;
		border: 0px;
	}
	.header_search
	{
		border: 0px;
		margin-right: 20px;
	}
	.header_bookmark{border: 0px;}
	.header__logo{text-align: center;}
	.header__logo-text { display: none; }
	.header__second-line{display: none;}
	.header__desctop-first-line{display: none;}
	@media (min-width: 768px)
	{
		.header__logo a{text-decoration: none;}
		.header__logo-text
		{
			display:block;
			color:#6C6C6C;
			font-family: 'Roboto';
			font-size: 11px;
		}
	}
	@media (min-width: 1200px)
	{
		.header__first-line{display: none;}
		.header__second-line
		{
			display: block;
			margin-top: 36px;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}
		.header__catalog
		{
			background: #FC4442;
			color: #fff;
			border:0px;
			width:170px;
			border-radius: 100px;
			text-align: center;
			font-size: 18px;
			display: flex;
			justify-content: center;
			align-items: center;
			height: 52px;
			svg{margin-right: 10px;}
			.header__catalog__close{display:none;}
			&.header__catalog--opened
			{
				background:#fff;
				color:#FC4442;
				border:1px solid #FC4442;
				.header__catalog__close{display:inline;}
				.header__catalog__burger{display:none;}
			}
		}
		.header__search-input
		{
			position:relative;
			input
			{
				border: 1px solid #EAEAEA;
				border-radius: 100px;
				height: 52px;
				padding-left: 30px;
				color: rgba(45, 45, 45, 0.5);
				box-sizing: border-box;
				width: 715px;
			}
			button
			{
				border: 0px;
				position: absolute;
				right: 26px;
				top: 16px;
			}
		}
		.header__big-buttons
		{
			display: flex;
			a
			{
				color: #2D2D2D;
				text-decoration: none;
				display: flex;
				align-items: center;
				&:first-child{margin-right:32px;}
				svg{margin-right: 8px;}
			}
		}
		.header__desctop-first-line
		{
			display: flex;
			justify-content: space-between;
		}
		.header__menu-small
		{
			ul{
				list-style: none;
				display: flex;
			}
			li{margin-right: 80px;}
			li:last-child{margin-right: 0px;}
			a
			{
				color:#6C6C6C;
				text-decoration: none;
			}
		}
		.header__phone
		{
			a
			{
				font-size: 16px;
				color:#2D2D2D;
				text-decoration: none;
			}
			span
			{
				display: block;
				margin-top: 8px;
				font-size: 13px;
				color: #2D2D2D;
				font-weight: 300;
			}
		}
		.header__desc-logo a{text-decoration: none;}
	}
</style>