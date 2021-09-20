<template>
	<div class="catalog-popup">
		<div class="container">
			<div
				class="catalog-popup__col"
				v-for="(catalogCol,catalogColIndex) in catalog"
				:key="catalogColIndex"
			>
				<ul>
					<li
						v-for="catalogItem in catalogCol"
						:key="catalogItem.link"
						:class="{active:catalogItem.active}"
						@mouseover="hoverItem(catalogCol,catalogItem)"
					>
						<NuxtLink  :to="catalogItem.link">{{ catalogItem.name }}</NuxtLink>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>
<script>
	export default
	{
		data()
		{
			return {
				catalog:[
					[
						{name:'Мягкая мебель',link:"/about/",active:false},
						{name:'Шкафы-купе',link:"/",active:false},
						{name:'Распашные шкафы',link:"/",active:false},
						{name:'Мебель для кухни',link:"/",active:false},
						{name:'Гостиные',link:"/",active:true},
						{name:'Комоды',link:"/",active:false},
						{name:'Спальни',link:"/",active:false},
						{name:'Кровати и тахты',link:"/",active:false},
						{name:'Матрасы, наматрасники',link:"/",active:false},
						{name:'Одеяла, подушки',link:"/",active:false},
						{name:'Мягкая мебель',link:"/",active:false},
					],
				]
			};
		},
		methods:
		{
			hoverItem(catalogCol,item)
			{
				catalogCol.map((item)=>{
					item.active = false;
				})
				item.active = true;
			}
		}
	}
</script>
<style lang="scss">
	.catalog-popup
	{
		padding-top:30px;
		position:absolute;
		z-index:10;
		background: #fff;
		width:100%;
		height: calc(100vh - 140px);
		.container{display: flex;}
	}
	.catalog-popup__col
	{
		border-right: 1px solid #EAEAEA;
		padding-right: 22px;
		padding-left: 18px;
		&:first-child { padding-left: 0px; }
		&:last-child { border-right: 0px; }
	}
	.catalog-popup__col ul
	{
		list-style: none;
		padding:0px;
		li { margin-bottom: 22px; }
		a
		{
			text-decoration: none;
			color:#2D2D2D;
			font-weight: 500;
			font-size: 20px;
		}
		.active a{color:#FC4442;}
	}
</style>