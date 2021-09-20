<template>
	<div class="filter">
		<div class="filter-background" @click="$emit('closeFilter')"/>
		<div class="filter-body">
			<ul>
				<li>Диваны и кресла</li>
				<li>Mobiles, Computers</li>
				<li>Movies, Music & Video Games</li>
				<li>Gift Cards & Mobile Recharges</li>
				<li>Car, Motorbike, Industrial</li>
			</ul>
			<div class="filter__accordion">
				<div class="filter__price">
					<div class="filter__accordion-item">
						<span>Цена, ₽</span>
						<svg-icon name="arrow-down"></svg-icon >
					</div>
					<div>
						<RangeSlider :rangeSliderData="rangeSliderData"/>
					</div>
				</div>
				<div class="filter__brand">
					<div class="filter__accordion-item">
						<span>Бренд</span>
						<svg-icon name="arrow-down"></svg-icon >
					</div>
					<div class="filter__accordion-content">
						<CheckBoxList id="1" :checkBoxListData="firstCheckBoxListData"/>
					</div>
				</div>
				<div class="filter__collection">
					<div class="filter__accordion-item">
						<span>Коллекция</span>
						<svg-icon name="arrow-down"></svg-icon >
					</div>
					<div class="filter__accordion-content">
						<CheckBoxList id="2" :checkBoxListData="secondCheckBoxListData"/>
					</div>
				</div>
			</div>
			<button class="filter-clear" @click="filterClear()">Очистить фильтр</button>
			<button class="filter-close" @click="$emit('closeFilter')"><svg-icon name="close" /></button>
		</div>
	</div>
</template>
<script>
	import RangeSlider from '@/components/RangeSlider';
	export default
	{
		components:
		{
			RangeSlider,
		},
		data()
		{
			return {
				firstCheckBoxListData:[
					{name:'Ахундова Алла', state:false},
					{name:'Бажов Павел', state:false},
					{name:'Баландин Бронислав', state:false},
					{name:'Балтер Борис', state:false},
					{name:'Берестов Валентин', state:false},
					{name:'Биник Кристиан', state:false},
					{name:'Блок Александр', state:false},
					{name:'Ахундова Алла', state:false},
					{name:'Бажов Павел', state:false},
					{name:'Баландин Бронислав', state:false},
					{name:'Балтер Борис', state:false},
					{name:'Берестов Валентин', state:false},
					{name:'Биник Кристиан', state:false},
					{name:'Блок Александр', state:false},
				],
				secondCheckBoxListData:[
					{name:'Ахундова Алла', state:false},
					{name:'Бажов Павел', state:false},
					{name:'Баландин Бронислав', state:false},
					{name:'Балтер Борис', state:false},
					{name:'Берестов Валентин', state:false},
					{name:'Биник Кристиан', state:false},
					{name:'Блок Александр', state:false},
					{name:'Ахундова Алла', state:false},
					{name:'Бажов Павел', state:false},
					{name:'Баландин Бронислав', state:false},
					{name:'Балтер Борис', state:false},
					{name:'Берестов Валентин', state:false},
					{name:'Биник Кристиан', state:false},
					{name:'Блок Александр', state:false},
				],
				rangeSliderData: {
					stateMinPrice:2500,
					stateMaxPrice:6500,
					maxValue:6500,
				},
			};
		},
		methods:
		{
			filterClear()
			{
				Object.assign(this.$data, this.$options.data.call(this));
			}
		}
	};
</script>
<style lang="scss">
	.filter
	{
		position: fixed;
		overflow: auto;
		top:0;
		left:0;
		width: 100vw;
		height: 100vh;
		z-index: 1000;
	}
	.filter-background
	{
		position:fixed;
		top:0;
		left:0;
		background: rgba(0,0,0,0.2);
		width: 100vw;
		height: 100vh;
	}
	.filter-body
	{
		position:absolute;
		top:0;
		left:0;
		background:white;
		min-width: 277px;
		min-height: 100vh;
		ul
		{
			margin: 0;
			padding: 20px 0 14px 18px;
			list-style: none;
		}
		li
		{
			color: #6C6C6C;
			font-size: 16px;
			font-weight: 400;
			line-height: 19px;
			margin-bottom: 10px;
		}
		li:first-child
		{
			color:#2D2D2D;
			font-weight: 500;
		}
	}
	.filter-close
	{
		position: absolute;
		top: 16px;
		right: 20px;
		width: 22px;
		height: 22px;
		border: none;
		svg
		{
			width: 22px;
			height: 22px;
		}
	}
	.filter__accordion > div
	{
		border-top: 1px solid #EAEAEA
	}
	.filter__accordion-item
	{
		display: flex;
		justify-content: space-between;
		padding:0 18px;
		height: 61px;
		align-items: center;
		font-size: 14px;
		svg
		{
			transform: rotate(180deg);
			width: 11.67px;
			height: 7px;
		}
	}
	.filter__price{padding-bottom: 32px;}
	.filter__accordion-content{ margin-left: 20px;}
	.filter__collection{ margin-bottom: 8px;}
	.filter-clear
	{
		display: inline-block;
		margin:0 16px 0 19px;
		min-width: 244px;
		height: 44px;
		color:#FC4442;
		background:#FEDAD9;
		border:none;
		border-radius:10px;
		font-size: 14px;
		font-weight: 500;
	}
	.filter-body{ padding-bottom: 34px;}
	@media (min-width: 1200px)
	{
		.filter
		{
			position: relative;
			top:unset;
			width: max-content;
			height: max-content;
			min-width: 277px;
			z-index: unset;
			border: 1px solid #ABABAB;
			border-radius: 10px;
		}
		.filter-body
		{
			position: static;
		}
		.filter-background{display: none;}
		.filter-close{display: none;}
	}
</style>