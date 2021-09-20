<template>
	<div class="detal-product">
		<a href="#" class="detal-product__button-back">
			<svg-icon name="Arrow-left" height="10" width="11" />
			<span>назад</span>
		</a>
		<ul class="detal-product__route">
			<li class="detal-product__route-item"><a href="#">VMebel</a></li>
			<li class="detal-product__route-item"><a href="#">Диваны и кресла</a></li>
			<li class="detal-product__route-item"><a href="#">Mobiles, Computers</a></li>
			<li class="detal-product__route-item"><a href="#">Чайная машина Kitfort KT-630</a></li>
		</ul>
		<h1>{{name}}</h1>
		<p>Артикул 100 024 215 307</p>
		<section class="detal-product__item">
			<Slider :images="sliderImagesUrl">
			</Slider>
			<div class="detal-product__shops-existence">
				<h3>Магазины с данным товаром</h3>
				<ul>
					<li>
						<div>
							<p>Johnson & Johnson</p>
							<p>ул. К. Либкнехта, д. 2, г.</p>
						</div>
						<svg-icon name="Arrow-down" height="15" width="10"/>
					</li>
					<li>
						<div>
							<p>Ferrari</p>
							<p>ул. Ленина, д. 40, г. Майкоп</p>
						</div>
						<svg-icon name="Arrow-down" height="15" width="10"/>
					</li>
					<li>
						<div>
							<p>IBM</p>
							<p>пр-т Калинина, д. 8, г. Барнаул</p>
						</div>
						<svg-icon name="Arrow-down" height="15" width="10"/>
					</li>
					<li>
						<div>
							<p>Starbucks</p>
							<p>ул. Лермонтова, д. 14, пом. 3</p>
						</div>
						<svg-icon name="Arrow-down" height="15" width="10"/>
					</li>
					<li>
						<div>
							<p>L'Oréal</p>
							<p>ул. Большая Московская, д.</p>
						</div>
						<svg-icon name="Arrow-down" height="15" width="10"/>
					</li>
				</ul>
				<a href="">Показать все магазины</a>
			</div>
		</section>

		<section class="detal-product__information">
			<div class="detal-product__buttons">
				<button class="detal-product__about-product detal-product__button-active">О товаре</button>
				<button class="detal-product__shops">Магазины</button>
				<button class="detal-product__statistics">Характеристики</button>
			</div>
			<div class="detal-product__information-text">
				<h3>Кресло рабочее Vivianne</h3>
				<p>Кресло Vivianne с сеточным каркасом сиденья и спинки поддерживает удобную рабочую позу на протяжении длительного времени. Лаконичный дизайн модели выдержан в стиле минимализма, подходящего для эргономичного офисного пространства. Форма спинки разработана с учетом анатомических особенностей позвоночника. Механизм качания и регулировка высоты сиденья дают возможность выбрать оптимальное положение для пользователя. За счет небольшого веса модели и стойки на колесах кресло можно свободно передвинуть в нужном направлении.</p>
				<h3>Характеристики</h3>
				<ul>
					<li>
						<span>Коллекция</span>
						<span class="detal-product__information-dicoration"></span>
						<span>Vivianne</span>
					</li>
					<li>
						<span>Производитель</span>
						<span class="detal-product__information-dicoration"></span>
						<span>Китай</span>
					</li>
					<li>
						<span>Гарантия</span>
						<span class="detal-product__information-dicoration"></span>
						<span>24 мес.</span>
					</li>
					<li>
						<span>Срок службы</span>
						<span class="detal-product__information-dicoration"></span>
						<span>Год: 5</span>
					</li>
					<li>
						<span>Размеры кресла (ШхВхГ)</span>
						<span class="detal-product__information-dicoration"></span>
						<span>54 х 107 х 65 см</span>
					</li>
					<li>
						<span>Цвет</span>
						<span class="detal-product__information-dicoration"></span>
						<span>серый</span>
					</li>
				</ul>
			</div>
		</section>
		<SubscribeForm />
	</div>
</template>
<script>
	import SubscribeForm from '@/components/SubscribeForm';
	import Slider from '@/components/Slider';
	export default
	{
		components: { SubscribeForm, Slider },
		data()
		{
			return {
				name:'Чайная машина Kitfort KT-630',
				sliderImagesUrl: [
					'/images/image-for-slider 1.png',
					'/images/image-for-slider 2.png',
					'/images/image-for-slider 4.png',
					'/images/image-for-slider 2.png',
					'/images/image-for-slider 1.png',
					'/images/image-for-slider 4.png',
				],
			};
		},

	};
</script>
<style lang='scss'>
	.detal-product
	{
		padding-top: 10px;
		h1
		{
			color:#2D2D2D;
			margin: 0;
			margin-bottom: 16px;
			font-family: Roboto;
			font-size:18px;
		}
		p
		{
			margin: 0;
			margin-bottom: 19px;
			color: #6C6C6C;
			font-family: Roboto;
			font-size: 12px;
			line-height: 14px;
		}
		& > p
		{
			margin-bottom: 18px;
		}
	}
	.detal-product__button-back
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
		svg
		{
			margin-right: 6px;
		}
	}
	.detal-product__route
	{
		margin: 0;
		margin-bottom: 18px;
		padding: 0;
	}
	.detal-product__route-item
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
	.detal-product__buttons button
	{
		border:none;
		font-size: 16px;
		line-height: 19px;
	}
	.detal-product__slider
	{
		position: relative;
		min-width: fit-content;
		margin-bottom: 8px;
		img
		{
			margin-bottom: 11px;
			width: 100%;
		}
	}
	.detal-product__buttons-slider button
	{
		position:absolute;
		top:34%;
		height: 30px;
		width:30px;
		background: #2D2D2D;
		color:white;
		border:none;
		border-radius:50%;
		&:first-of-type
		{
			left:0;
		}
		&:last-of-type
		{
			right:0;
		}
	}
	.detal-product__pages
	{
		text-align: center;
		height: 40px;
		.detal-product__page
		{
			display: inline-block;
			height: 8px;
			width: 8px;
			background-color:#2D2D2D;
			border-radius:50%;
			margin-right: 10px;
			margin: 0 3px;
		}
		.detal-product__images{ display: none;}
	}
	.detal-product__shops-existence
	{
		margin-bottom: 17px;
		border: 1px solid #EAEAEA;
		border-radius: 20px;
		padding-top: 25px;
		h3
		{
			margin: 0;
			padding-left: 15px;
			color:#969696;
			text-transform:uppercase;
			font-size:14px;
			font-weight: normal;
			line-height: 16px;
		}
		ul
		{
			list-style: none;
			padding: 0;
			margin: 0;
			padding-top: 10px;
			margin-bottom: 25px;
		}
		li
		{
			display: flex;
			justify-content: space-between;
			align-items:center;
			border-bottom: 1px solid #EAEAEA;
			height: 71px;
			padding: 0 15px;
		}
		div p:first-child
		{
			margin: 0;
			margin-bottom: 5px;
			color:#2D2D2D;
			font-size: 16px;
			font-weight: normal;
			line-height: 19px;
		}
		div p:last-child
		{
			margin: 0;
			color:#6C6C6C;
			font-size: 14px;
			font-weight: 500;
			line-height: 16px;
		}
		a
		{
			display: block;
			margin: 0 16px 30px 16px;
			height: 44px;
			border-radius:10px;
			text-align: center;
			text-decoration: none;
			color: #FC4442;
			background:#FEDAD9;
			line-height: 44px;
			font-size: 14px;
			font-weight: normal;
		}
	}
	.detal-product__buttons
	{
		border-radius:10px;
		border: 1px solid #EAEAEA;
		height: 64px;
		line-height: 64px;
		white-space: nowrap;
		margin-bottom: 20px;
		button
		{
			color: #969696;
			font-size: 12px;
			font-weight: normal;
			line-height: 14px;
			height: 100%;
			width: 33%;
		}
		.detal-product__button-active
		{
			color:#2D2D2D;
			font-size: 12px;
			font-weight: normal;
			line-height: 14px;
		}
	}
	.detal-product__information-text
	{
		margin: 0;
		margin-bottom: 20px;
		padding: 0;
		ul
		{
			padding-left: 1px;
			margin: 0;
		}
		li
		{
			display: flex;
			justify-content: space-between;
			margin-bottom: 17px;
			max-width: 973px;
			span
			{
				color: #6C6C6C;
				font-size: 16px;
				font-weight: normal;
				line-height: 19px;
				white-space: nowrap;
			}
		}
		h3
		{
			margin: 0;
			margin-bottom: 16px;
			color: #2D2D2D;
			font-size: 18px;
			font-weight: 500;
			line-height: 21px;
			&:last-of-type
			{
				margin-bottom: 20px;
			}
		}
		p
		{
			font-size: 16px;
			font-weight: 400;
			line-height: 24px;
			margin-bottom: 21px;
		}
		.detal-product__information-dicoration
		{
			display: block;
			width: 100%;
			border-bottom: 1px dashed #ABABAB;
			margin: 0 7px 6px 7px;
		}
	}
	@media (min-width: 768px) {
		.detal-product__button-back
		{
			margin-bottom: 16px;
		}
		.detal-product
		{
			padding-top: 6px;
		}
		.detal-product__route-item
		{
			font-size: 14px;
			font-weight: 400;
		}
		.detal-product h1
		{
			margin-bottom: 6px;
			font-size: 26px;
			font-weight: 700;
			line-height: 30px;
		}
		.detal-product p
		{
			font-size: 14px;
			line-height: 16px;
			margin-bottom: 40px;
		}
		.detal-product__slider
		{
			position: relative;
			min-width: fit-content;
			margin-bottom: 40px;
			img{ margin-bottom: 11px;}
		}
		.detal-product__pages
		{
			display: flex;
			height: 82px;
			.detal-product__page{ display: none;}
			.detal-product__images
			{
				display: block;
				img{ width: 15%}
			}
		}
		.detal-product__buttons-slider button
		{
			top:unset;
			bottom: 20px;
		}
		.detal-product__buttons
		{
			margin-bottom: 32px;
		}
		.detal-product__buttons button
		{
			width: 130px;
			font-size: 16px;
			font-weight: 400;
			line-height: 19px;
			&.detal-product__button-active
			{
				width: 130px;
				font-size: 16px;
				font-weight: 400;
				line-height: 19px;
			}
		}
		.detal-product__information p
		{
			font-weight: 400;
			line-height: 24px;
			font-size: 16px;
			padding-left: 1px;
			margin-bottom: 61px;
		}
		.detal-product__information h3
		{
			margin-bottom: 13px;
		}
		.detal-product__information-text{ margin-bottom: 40px;}
		.detal-product__route-item:not(:last-of-type)::after
		{
			margin-right: 5px;
			margin-left: 11px;
		}
		.detal-product__shops-existence
		{
			padding-top: 23px;
			margin-bottom: 40px;
			h3
			{
				padding-left: 30px;
			}
			li
			{
				padding: 0 30px;
			}
			a
			{
				margin: 0 22px 30px 26px;
			}
		}
	}
	@media (min-width: 1440px) {
		.detal-product
		{
			padding-top: 22px;
		}
		.detal-product > p
		{
			margin-bottom: 20px;
		}
		.detal-product__button-back{ display: none;}
		.detal-product__item
		{
			display: flex;
			flex-direction:row;
			align-items: flex-start;
			margin-bottom: 56px;
		}
		.detal-product__shops-existence
		{
			min-width: unset;
			width: 380px;
			li
			{
				padding: 0;
				padding-left: 24px;
				padding-right:23px;
			}
		}
		.detal-product__pages{ display: flex;}
		.detal-product__slider
		{
			max-width: 778px;
			width: 100%;
			margin-right: 22px;
		}
		.detal-product__images
		{
			max-width: 728px;
			width: 100%;
		}
		.detal-product__information-text{ margin-bottom: 402px;}
		.detal-product__buttons
		{
			margin-bottom: 46px;
		}
		.detal-product__information p
		{
			margin-bottom: 30px;
		}
		.detal-product__information-text div
		{
			padding-left: 5px;
		}
	}
</style>