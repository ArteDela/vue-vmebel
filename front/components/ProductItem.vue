<template>
	<section class="product-item">
		<a class="product-item__image" :href="productData.href" >
			<picture>
				<source :srcset="productData.imgSrcMobile" media="(max-width: 767px)">
				<img :src="(productData.imgSrc)? productData.imgSrc :'/images/product-image.png'" alt="">
			</picture>
		</a>
		<div v-if="(productData.price)"class="product-item__price">{{productData.price}}</div>
		<a class="product-item__name" :href="productData.href">{{productData.productName}}</a>
		<br />
		<a
			class="product-item__shop-exist"
			:href="productData.href"
			v-if="(productData.shopExist)"
		>
			Представлен в {{productData.shopExist}} магазинах
		</a>
		<button @click='productData.favorites = !productData.favorites'>
			<svg-icon
				:name="(productData.favorites) ? 'Book-mark': 'Book-mark-off'"
			/>
		</button>
	</section>
</template>
<script>
	export default
	{
		props: {
			productData:Object,
		},
		methods:
		{
			test(){
				console.log(this.productData)
			}
		}
	}
</script>
<style lang="scss">
	.product-item
	{
		position: relative;
		max-width: 142px;
		min-width: 125px;
		max-height: 306px;
		border: 1px solid #EAEAEA;
		border-radius: 10px;
		padding: 9px 12px 6px 13px;
		color: #2D2D2D;
		button
		{
			position: absolute;
			top: 10px;
			right: 10px;
			height: 22px;
			width: 24px;
			border:none;
			border-radius: 50%;
			background: white;
			box-shadow: 0px 1px 3px 0px #00000017;
			padding: 3px;
		}
		button svg
		{
			height: 14px;
			width: 15px;
		}
		img
		{
			min-width: 142px;
			width: 100%;
		}
		picture { display: inline-block;}
	}
	.product-item__image{ margin-bottom: 6px;}
	.product-item__price
	{
		color:#2D2D2D;
		margin-bottom: 2px;
		font-size: 12px;
		font-weight: 500;
		line-height: 14px;
	}
	.product-item__name
	{
		color:#2D2D2D;
		text-decoration: none;
		display: inline-block;
		margin-bottom: 2px;
		white-space: nowrap;
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
	.product-item__shop-exist
	{

		font-size: 10px;
		line-height: 12px;
		text-decoration: none;
		color:#6C6C6C;
		max-width: 230px;
		&:hover
		{
			text-decoration: underline;
		}
	}
	@media(min-width: 768px)
	{
		.product-item
		{
			max-width: unset;
			min-width: unset;
			width: 195px;
			max-height: 306px;
			padding: 14.83px 17.31px 13px 18.96px;
			button
			{
				top: 10px;
				right: 10px;
				height: 35.7px;
				width: 33.8px;
				padding: 7px;
			}
			button svg
			{
				height: 21px;
				width: 21px;
			}
			img
			{
				min-width: 193px;
				min-height: 193px;
			}
		}
		.product-item__image{ margin-bottom: 13px;}
		.product-item{ padding: 14px 17px 15px 18px;}
		.product-item img
		{
			min-width:193px;
			width: 100%
		}
		.product-item__price
		{
			font-size: 18px;
			line-height: 21px;
			margin-bottom: 4px;
		}
		.product-item__name
		{
			font-size: 12px;
			font-weight: 400;
			line-height: 14px;
			margin-bottom: 6px;
		}
		.product-item__shop-exist
		{
			font-size: 14px;
			font-weight: normal;
			line-height: 16px;
		}
	}
	@media(min-width: 1200px)
	{
		.product-item
		{
			padding: 17px 21px 20px 23px;
			min-width: 235px;
			img
			{
				min-width: 235px;
			}
			button
			{
				top: 10px;
				right: 10px;
				height: 41px;
				width: 41px;
				padding: 8px ​8px 5px 8px;
			}
			svg
			{
				height: 24px;
				width:24px;
			}
		}
		.product-item__name
		{
			font-size: 14px;
			line-height: 16px;
		}
		.product-item__image
		{
			display: block;
			margin-bottom: 13px;
		}
	}
</style>