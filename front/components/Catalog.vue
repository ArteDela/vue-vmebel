<template>
	<div class="catalog">
		<ul class="catalog__list" v-if="isDesktop">
			<li
				class="list__item"
				v-for="result in catalogs"
				:key="result.name"
			>
				<div class="list__item-name">{{result.name}}</div>
				<NuxtLink
					:to="resChildren.url"
					class="list__item-link"
					v-for="resChildren in result.children"
					:key="resChildren.name"
				>
					{{resChildren.name}}
				</NuxtLink>
			</li>
		</ul>
		<div class="catalog__link">
			<NuxtLink
				:to="result.url"
				class="catalog__link-item"
				v-for="(result, index) in catalogs"
				:key="index"
			>
				<div class="catalog__link-image">
					<img :src="(result.picture)? result.picture : '/images/NoImage.png'" alt="">
				</div>
				<p class="catalog__link-name">{{result.name}}</p>
			</NuxtLink>
		</div>
	</div>
</template>
<script>
	import { mapActions, mapGetters } from 'vuex'
	export default
	{
		data()
		{
			return {
				isDesktop:false,
			}
		},
		methods:
		{
			...mapActions('catalog',[
				'getCatalogs'
			]),
			onResize() {
				this.isDesktop = window.innerWidth > 1200
			}
		},
		mounted() {
			this.onResize()
			window.addEventListener('resize', this.onResize)
		},
		computed:
		{
			...mapGetters('catalog',[
				'catalogs'
			])
		},
		async fetch()
		{
			await this.getCatalogs()
		}
	}
</script>

<style>
	.catalog
	{
		display: flex;
		margin-bottom: 29px;
	}
	.catalog__list
	{
		list-style-type: none;
		flex-basis: 33.9%;
		padding: 0;
		margin: 0;
		margin-right: 21px;
		border: 1px solid #ABABAB;
		border-radius: 10px;
	}
	.catalog__link
	{
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(165px, 1fr));
		grid-gap:4px;
		width: 100%;
	}
	.catalog__link-item
	{
		border: 1px solid #EAEAEA;
		border-radius: 10px;
		padding: 14px 24px 18px 16px;
		text-decoration: none;
		display: block;
	}
	.catalog__link-image
	{
		width: 128px;
		height: 136px;
		margin: 0 auto;
		margin-bottom: 15px;
	}
	.catalog__link-image img
	{
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
	.catalog__link-name
	{
		font-weight: bold;
		font-size: 10px;
		line-height: 12px;
		color: #2D2D2D;
		text-align: center;
	}
	@media (min-width: 768px)
	{
		.catalog__link
		{
			grid-gap:17px;
			grid-template-columns: repeat(auto-fit, minmax(231px, 1fr));
		}
		.catalog__link-name
		{
			font-size: 14px;
			line-height: 16px;
		}
	}
	@media (min-width: 1024px)
	{
		.catalog__link{ grid-auto-rows: min-content;}
		.catalog{margin-bottom: 40px;}
		.catalog__list .list__item
		{
			padding-left: 18px;
			padding-right: 10px;
			padding-top: 19px;
		}
	}
</style>