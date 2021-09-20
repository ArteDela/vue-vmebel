<template>
	<div class="favorites">
		<a href="#" class="favorites__button-back">
			<svg-icon name="Arrow-left" height="10" width="11" />
			<span>назад</span>
		</a>
		<ul class="favorites__route">
			<li class="favorites__route-item"><a href="#">VMebel</a></li>
			<li class="favorites__route-item"><a href="#">Избраные товары</a></li>
		</ul>
		<h1>Избранные товары</h1>
		<div class="favorites__content">
			<ProductItem v-for="item of categoryContent" :productData="item"></ProductItem>
		</div>
		<SubscribeForm />
	</div>
</template>

<script>
	import SendBanner from '@/components/SendBanner';
	import SubscribeForm from '@/components/SubscribeForm';
	import ProductItem from '@/components/ProductItem';
	export default
	{
		components:
		{
			SendBanner,
			SubscribeForm,
			ProductItem,
		},
		data() {
			return {
				categoryContent: [
					{
						imgSrc: '/images/product-image.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '110 ₽',
						productName: 'Coach Tabby 26 for sale',
						shopExist: 4,
						favorites: true,
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
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-1.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '60 ₽',
						productName: 'Heimer Miller Sofa (Mint Condition)',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-3.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '310 ₽',
						productName: 'Air Jordan 1 Top 3 Sneaker (DS)',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-5.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '240 ₽',
						productName: 'Gopro hero 7 (with receipt)',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '110 ₽',
						productName: 'Coach Tabby 26 for sale',
						shopExist: 4,
						favorites: true,
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
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-1.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '60 ₽',
						productName: 'Heimer Miller Sofa (Mint Condition)',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-3.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '310 ₽',
						productName: 'Air Jordan 1 Top 3 Sneaker (DS)',
						shopExist: 4,
						favorites: true,
					},
					{
						imgSrc: '/images/product-image-5.png',
						imgSrcMobile: '/images/product-image-mobile-1.png',
						href: '#',
						price: '240 ₽',
						productName: 'Gopro hero 7 (with receipt)',
						shopExist: 4,
						favorites: true,
					},
				],
			}
		}
	}
</script>
<style lang="scss">
	.favorites
	{
		padding-top: 36px;
		min-height:100vh;
		h1
		{
			font-family: Roboto;
			font-size: 18px;
			font-style: normal;
			font-weight: 700;
			line-height: 21px;
			margin:0;
			margin-bottom: 34px;
		}
	}
	.favorites__route
	{
		margin: 0;
		margin-bottom: 18px;
		padding: 0;
	}
	.favorites__route-item
	{
		display: inline;
		font-family: Roboto;
		color:#6C6C6C;
		font-weight: 400;
		font-size: 8px;
		line-height: 9px;
		a{text-decoration:none;}
		&:first-of-type{font-weight: 700;}
		&:last-of-type{color:#2D2D2D;}
		&:not(:last-of-type)::after
		{
			content: '';
			display: inline-block;
			height: 1px;
			width: 11px;
			margin-bottom: 3px;
			margin-right: 1px;
			margin-left: 4px;
			border-bottom: 1px solid #6C6C6C;
		}
	}
	.favorites__button-back
	{
		display: inline-block;
		text-decoration: none;
		height: 10px;
		font-size: 8px;
		font-weight: normal;
		line-height: 10px;
		margin-bottom: 10px;
		span
		{
			display: inline-block;
			vertical-align: top;
			height: 100%;
			margin-right: 7px;
		}
		svg{ margin-right: 6px;}
	}
	.favorites__content
	{
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(165px, 1fr));
		grid-gap: 13px;
		margin-bottom: 20px;
	}
	.favorites__item
	{
		display: flex;
		position: relative;
		flex-direction: column;
		justify-content: flex-start;
		align-items: flex-start;
		max-width: 279px;
		min-width: 125px;
		max-height: 306px;
		border: 1px solid #EAEAEA;
		border-radius: 10px;
		padding: 9px 12px 14px 7px;
		color: #2D2D2D;
		button
		{
			position: absolute;
			top: 10px;
			right: 10px;
			height: 41px;
			width: 41px;
			border:none;
			border-radius: 50%;
			background: white;
			box-shadow: 0px 1px 3px 0px #00000017;
			padding-top: 5px;
		}
		button svg
		{
			height: 24px;
			width: 24px;
		}
		img
		{
			margin-bottom: 13px;
			min-width: 142px;
			width: 100%;
		}
	}
	.favorites__price
	{
		color:#2D2D2D;
		font-size: 18px;
		font-weight: 500;
		line-height: 21px;
		margin-bottom: 7px;
	}
	.favorites__name
	{
		color:#2D2D2D;
		text-decoration: none;
		display: inline-block;
		margin-bottom: 7px;
		font-weight: 400;
		font-size: 9px;
		line-height: 11px;
		letter-spacing: 0em;
		text-align: left;

		&:hover
		{
			text-decoration: underline;
		}
	}
	.favorites__shop-exist
	{

		font-size: 10px;
		line-height: 12px;
		text-decoration: none;
		color:#6C6C6C;
		&:hover
		{
			text-decoration: underline;
		}
	}
	@media(min-width: 768px)
	{
		.favorites__item img
		{
			min-width:193px;
			width: 100%
		}
		.favorites__content
		{
			grid-template-columns: repeat(auto-fit, minmax(231px, 1fr));
			grid-gap: 19px;
		}
		.favorites__route-item
		{
			font-size: 14px;
			font-weight: 400;
		}
		.favorites__route-item:not(:last-of-type)::after
		{
			margin-right: 5px;
			margin-left: 11px;
		}
		.favorites__button-back
		{
			margin-bottom: 16px;
		}
		.favorites__price
		{
			font-size: 18px;
			line-height: 21px;
		}
		.favorites__name
		{
			font-size: 12px;
			font-weight: 400;
			line-height: 14px;
		}
		.favorites__shop-exist
		{
			font-size: 14px;
			font-weight: normal;
			line-height: 16px;
		}
		.favorites__item { padding: 14px 17px 15px 18px;}
	}
	@media(min-width: 1200px)
	{
		.favorites__item
		{
			padding: 17px 21px 20px 23px;
			img
			{
				min-width: 235px;
			}
		}
		.favorites__content{ grid-gap:19px 20px;}
		.favorites__name
		{
			font-size: 14px;
			line-height: 16px;
		}
		.favorites__button-back
		{
			display: none;
		}
		.favorites h1
		{
			font-size: 26px;
			line-height: 30px;
		}
	}
</style>
