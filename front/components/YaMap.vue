<template>
	<div class="yamap">
		<yandex-map
			:settings="settings"
			:coords="coords"
			zoom="14"
			style="width: 100%; height: 600px;"
		>
			<ymap-marker
				v-for="(marker,markerId) of markerParams"
				:marker-id="markerId"
				marker-type="placemark"
				:coords="marker.coords"
				:balloon="{header: marker.balloon[0], body: marker.balloon[1],
				footer: `<div class='yamap__buttons'><a href='${marker.href}' class='yamap__button'>Instagram</a> <a href='tel:${marker.number}' class='yamap__button'>Позвонить</a><div>`}"
				:icon="{ layout: 'default#image', imageHref: '/images/PlaceMarkIcon.svg', imageSize: [48, 70], imageOffset: [-20, -20]}"
				cluster-name="1"
			></ymap-marker>
		</yandex-map>
	</div>
</template>

<script>
	export default {
		props:{
			settings:Object,
			coords:Array,
			markerParams:Array,
		},
	}
</script>
<style lang="scss">
	.yamap__button
	{
		display: inline-block;
		height: 34px;
		width: 108px;
		border: 1px solid #EAEAEA;
		border-radius: 5px;
		font-size: 12px;
		font-weight: 400;
		line-height: 34px;
		text-align: center;
		vertical-align: middle;
		text-decoration: none;
		color:#2D2D2D;
		&:first-child{ margin-right:20px;}
	}
	ymaps[class$="balloon-content__footer"]
	{
		margin: 0;
		padding-top: 27px;
		padding-left: 67px;
	}
	ymaps[class$="balloon__content"]
	{
		color:#6C6C6C;
		font-size: 14px;
		font-weight: 400;
		line-height: 16px;
		ymaps[class$="balloon-content__header"]
		{
			color: #2D2D2D;
			font-weight: 700;
			line-height: 19px;
			margin-bottom: 7px;
		}
	}
</style>