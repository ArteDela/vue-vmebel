<template>
	<ul class="mobile-menu list">
		<li class="mobile-menu__close" @click="close">
			<svg width="23" height="22" viewBox="0 0 23 22" fill="none" xmlns="http://www.w3.org/2000/svg">
				<path d="M17.3594 4.8125L4.98438 17.1875" stroke="#6C6C6C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
				<path d="M17.3594 17.1875L4.98438 4.8125" stroke="#6C6C6C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			</svg>
		</li>
		<li class="list__item" v-for="result in CATALOGS" :key="result.name">
			<div class="list__item-name">{{result.name}}</div>
			<NuxtLink :to="result.url" class="list__item-link" v-for="resChildren in result.children" :key="resChildren.name">{{resChildren.name}}</NuxtLink>
		</li>
	</ul>
</template>
<style>
	.list
	{
		position: absolute;
		width: 90%;
		left: -100%;
		top: 0;
		background: white;
		padding: 0;
		margin: 0;
		z-index: 5;
		transition: .3s;
		height: 100vh;
		overflow: hidden;
		overflow-y: scroll;
	}
	.list::-webkit-scrollbar{width: 0;}
	.list .mobile-menu__close
	{
		list-style-type: none;
		position: absolute;
		top: 19px;
		right: 20px;
	}
	.list.active
	{
		transition: .3s;
		left: 0;
	}
	.list__item
	{
		padding-top: 23px;
		padding-left: 16px;
		padding-bottom: 36px;
		border-bottom: 1px solid #EAEAEA;
	}
	.list__item-name,
	.list__item-link
	{
		font-family: 'Roboto';
		font-size: 16px;
		line-height: 19px;
	}
	.list__item-name
	{
		color: #2D2D2D;
		margin-bottom: 16px;
		font-weight: bold;
	}
	.list__item-link
	{
		display: inline-block;
		color: #6C6C6C;
		font-weight: 500;
		text-decoration: none;
	}
	.list__item-link:not(:last-child){margin-bottom: 16px;}
	@media (min-width: 768px)
	{
		.list{width: 40%;}
	}
</style>
<script>
	import axios from 'axios'
	import { mapActions, mapGetters } from 'vuex'
	export default
	{
		props:['res'],
		data()
		{
			return {
			}
		},
		methods:
		{
			...mapActions('catalog',[
				'GET_CATALOGS'
			]),
			close()
			{
				this.$emit('close')
			}
		},
		computed:
		{
			...mapGetters('catalog',[
				'CATALOGS'
			])
		},
		async fetch()
		{
			await this.GET_CATALOGS()
		},
	}
</script>
