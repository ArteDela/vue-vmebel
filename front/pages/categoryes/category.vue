<template>
	<div class="category">
		<a href="#" class="category__button-back">
			<svg-icon name="Arrow-left" height="10" width="11" />
			<span>назад</span>
		</a>
		<ul class="category__route">
			<li class="category__route-item"><a href="#">VMebel</a></li>
			<li class="category__route-item"><a href="#">Диваны и кресла</a></li>
			<li class="category__route-item"><a href="#">Mobiles, Computers</a></li>
		</ul>
		<h1>
			Диваны и кресла
		</h1>
		<p>
			Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.
		</p>
		<main class="category__main">
			<button class="category__button-filter" @click="filterDisplay = true">
				<svg-icon name="setting"/>
				<span>Фильтр</span>
			</button>
			<CotegoryFilter
				class="category__filter"
				v-show='filterDisplay'
				@closeFilter="filterDisplay = false"
			/>
			<div class="category__content">
				<ProductItem
					v-for="(item, index) in categoryContent"
					:key="index"
					:productData="item"
				/>
			</div>
		</main>
		<SubscribeForm />
	</div>
</template>
<script>
	import ProductItem from '@/components/ProductItem';
	import CheckBoxList from '@/components/CheckBoxList';
	import CotegoryFilter from '@/components/CotegoryFilter';
	import SubscribeForm from '@/components/SubscribeForm';
	import SendBanner from '@/components/SendBanner';
	export default
	{
		components:
		{
			ProductItem,
			CheckBoxList,
			CotegoryFilter,
			SubscribeForm,
			SendBanner,
		},
		data() {
			return{
				filterDisplay:false,
				categoryContent: [
					{
						imgSrc: '/images/product-image.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '110 ₽',
						productName: 'Coach Tabby 26 for sale',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-2.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '400 ₽',
						productName: 'iPad Pro 2017 Model',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-4.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '600 ₽',
						productName: 'Macbook Pro 16 inch (2020 ) For Sale',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-1.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '60 ₽',
						productName: 'Heimer Miller Sofa (Mint Condition)',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-3.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '310 ₽',
						productName: 'Air Jordan 1 Top 3 Sneaker (DS)',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-5.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '240 ₽',
						productName: 'Gopro hero 7 (with receipt)',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '110 ₽',
						productName: 'Coach Tabby 26 for sale',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-2.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '400 ₽',
						productName: 'iPad Pro 2017 Model',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-4.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '600 ₽',
						productName: 'Macbook Pro 16 inch (2020 ) For Sale',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-1.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '60 ₽',
						productName: 'Heimer Miller Sofa (Mint Condition)',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-3.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '310 ₽',
						productName: 'Air Jordan 1 Top 3 Sneaker (DS)',
						shopExist: 4,
						favorites: false,
					},
					{
						imgSrc: '/images/product-image-5.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '240 ₽',
						productName: 'Gopro hero 7 (with receipt)',
						shopExist: 4,
						favorites: false,
					},
				],
				isDesktop:false,
			};
		},
		mounted() {
			this.onResize()
			window.addEventListener('resize', this.onResize)
		},
		methods: {
		    onResize() {
				this.isDesktop = window.innerWidth > 1200
			}
		},
		watch: {
			isDesktop: function() {
				this.filterDisplay = this.isDesktop;
			}
		}
	}
</script>
<style lang="scss">
	.category
	{
		min-height: 100vh;
		padding-top: 12px;
		margin-bottom: 30px;
		h1
		{
			margin: 0;
			margin-bottom: 10px;
			color:#2D2D2D;
			font-size: 26px;
			font-weight: 700;
			line-height: 30px;
		}
		&>p
		{
			display: inline-block;
			max-width: 747px;
			color: #6C6C6C;
			font-size: 16px;
			line-height: 19px;
			margin: 0;
			margin-bottom: 25px;
		}
	}
	.category__button-back
	{
		display: inline-block;
		text-decoration: none;
		height: 10px;
		font-size: 8px;
		font-weight: normal;
		margin-bottom: 17px;
		line-height: 9px;
		span
		{
			display: inline-block;
			vertical-align: top;
			height: 100%;
			margin-right: 7px;
		}
		svg
		{
			margin-right: 6px;
		}
	}
	.category__route
	{
		margin: 0;
		margin-bottom: 18px;
		padding: 0;
	}
	.category__route-item
	{
		display: inline;
		font-family: Roboto;
		color:#6C6C6C;
		font-size: 14px;
		font-weight: 400;
		line-height: 16px;
		a{text-decoration:none;}
		&:first-of-type{font-weight: 700;}
		&:last-of-type{color:#2D2D2D;}
		&:not(:last-of-type)::after
		{
			content: '';
			display: inline-block;
			height: 1px;
			width: 11px;
			margin-bottom: 4px;
			margin-right: 5px;
			margin-left: 11px;
			border-bottom: 1px solid #6C6C6C;
		}
	}
	.category__content
	{
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(165px, 1fr));
		grid-gap: 13px;
	}
	.category__button-filter
	{
		align-self:flex-end;
		margin-bottom: 23px;
		border:none;
		font-size: 13px;
		line-height: 13px;
		span
		{
			vertical-align: top;
			line-height: 32px;
			color: #6C6C6C;
			font-size: 13px;
		}
		svg
		{
			height: 32px;
			width:32px;
			margin-right: 4px;
		}
	}
	.category__main
	{
		margin-bottom: 30px;
		display: flex;
		flex-direction: column;
	}
	@media (min-width: 768px)
	{
		.category
		{
			margin-bottom: 40px;
			&>p { margin-bottom: 15px;}
		}
		.category__button-filter
		{
			margin-right: 5px;
			margin-bottom: 13px;
		}
		.category__content
		{
			grid-template-columns: repeat(auto-fit, minmax(231px, 1fr));
			grid-gap: 19px;
		}
		.category__button-back{ margin-bottom: 16px;}
		.category__route-item
		{
			font-size: 14px;
			font-weight: 400;
		}
		.category__route-item:not(:last-of-type)::after
		{
			margin-right: 5px;
			margin-left: 11px;
		}
		.category__main{ margin-bottom: 40px;}
	}
	@media (min-width: 1200px)
	{
		.category__content
		{
			grid-template-columns: repeat(auto-fit, 279px);
			grid-gap: 19px;
		}
		.category
		{
			margin-bottom: 151px;
			&>p
			{
				margin-bottom: 31px;
			}
		}
		.category__button-back{ display: none;}
		.category__content
		{
			width: 100%;
			grid-gap:19px 20px;
		}
		.category__button-filter{ display: none;}
		.category__main
		{
			display: flex;
			flex-direction: row;
			margin-bottom: 151px;
		}
		.category__filter{ margin-right: 2px}
	}
</style>