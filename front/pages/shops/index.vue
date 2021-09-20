<template>
	<div class="shops">
		<ul class="shops__route">
			<li class="shops__route-item"><a href="#">VMebel</a></li>
			<li class="shops__route-item"><a href="#">Магазины</a></li>
		</ul>
		<h1>Магазины</h1>
		<YandexMap
			class="shops__map"
			:settings="settings"
			:coords="coords"
			:markerParams="Markers"
		></YandexMap>
		<SubscribeForm></SubscribeForm>
	</div>
</template>

<script>
	import YandexMap from '@/components/YaMap';
	import SubscribeForm from '@/components/SubscribeForm';
	export default {
		components:{YandexMap, SubscribeForm},
		data(){
			return {
				settings: {
					apiKey: 'cdb5f773-967d-489a-967b-fee0e3104400',
					lang: 'ru_RU',
					coordorder: 'latlong',
					version: '2.1',
					debug: true,
				},
				coords:[43.05053175538191,44.66492080273346],
				Markers:[
					{
						imgSrc:'/images/PlaceMarkIcon.svg',
						coords: [43.05205665795814,44.67145126338105],
						balloon: ['Мебель Викалина','Кухни ️Гостиные ️Комоды Матрасы'],
						href: '#',
						number:'88888888888',
					},
					{
						imgSrc:'/images/PlaceMarkIcon.svg',
						coords: [43.05163886656211,44.6539147848254],
						balloon: ['Мебель Викалина','Спальни ️Гостиные ️Комоды Матрасы'],
						href: '#',
						number:'88888888888',
					},
					{
						imgSrc:'/images/PlaceMarkIcon.svg',
						coords: [43.03841647326532,44.65420217971782],
						balloon: ['Мебель Викалина','Спальни ️Кухни ️Гостиные ️Комоды'],
						href: '#',
						number:'88888888888',
					},
					{
						imgSrc:'/images/PlaceMarkIcon.svg',
						coords: [43.05799753453784,44.6429858653632],
						balloon: ['Мебель Викалина','Спальни ️Кухни ️Гостиные Матрасы'],
						href: '#',
						number:'88888888888',
					},
				]
			}
		},
	}
</script>
<style lang="scss">
	.shops h1
	{
		font-size: 26px;
		font-weight: 700;
		line-height: 30px;
		margin: 0;
		margin-bottom: 49px;
	}
	.shops__route
	{
		margin: 0;
		margin-bottom: 18px;
		padding: 0;
		padding-top: 36px;
	}
	.shops__route-item
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
	.shops__map
	{
		margin-bottom: 180px;
	}
	@media(min-width: 768px)
	{
		.shops__route-item
		{
			font-size: 14px;
			font-weight: 400;
		}
		.shops__route-item:not(:last-of-type)::after
		{
			margin-right: 5px;
			margin-left: 11px;
		}
	}
</style>