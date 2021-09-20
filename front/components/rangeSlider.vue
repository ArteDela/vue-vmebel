<template>
	<div class="range-slider">
		<div class="range-slider__input-places">
			<div class="range-slider__input-place">
				<span>от</span>
				<input
					type="number"
					v-model.number="rangeSliderData.stateMinPrice"
					@input="valideTest($event, 'stateMinPrice'), changeStateMaxPrice()"
				>
			</div>
			<div class="range-slider__decoration" />
			<div class="range-slider__input-place">
				<span>до</span>
				<input
					type="number"
					v-model.number="rangeSliderData.stateMaxPrice"
					@input="valideTest($event, 'stateMaxPrice'), changeStateMinPrice()"
				>
			</div>
		</div>
		<div class="range-slider__multi-range">
			<input
				type="range"
				value="25"
				v-model.number="rangeSliderData.stateMinPrice"
				@input="minPriceThumbCollision()"
				:max="maxValue"
			>
			<input
				type="range"
				value="75"
				v-model.number="rangeSliderData.stateMaxPrice"
				@input="maxPriceThumbCollision()"
				:max="maxValue"
			>
			<div class="range-slider__thumb" :style="{'left': (rangeSliderData.stateMinPrice / maxValue * 92.6) + '%'}" />
			<div class="range-slider__thumb" :style="{'left': (rangeSliderData.stateMaxPrice / maxValue * 92.6) + '%'}" />
			<div
				class="range-slider__difference-strip"
				:style="{'left':(rangeSliderData.stateMinPrice / maxValue * 92.6) + '%', 'width':((rangeSliderData.stateMaxPrice / maxValue * 92.6)-(rangeSliderData.stateMinPrice / maxValue * 92.6))+'%'  }"
			/>
		</div>
	</div>
</template>
<script>
	export default
	{
		props:
		{
			rangeSliderData:Object,
		},
		data()
		{
			return{
				stateMinPrice:2500,
				stateMaxPrice:6500,
				maxValue:6500,
			};
		},
		methods:
		{
			minPriceThumbCollision()
			{
				this.rangeSliderData.stateMinPrice = (this.rangeSliderData.stateMinPrice >= this.rangeSliderData.stateMaxPrice) ? this.rangeSliderData.stateMaxPrice - 1 : this.rangeSliderData.stateMinPrice;
			},
			maxPriceThumbCollision(){
				this.rangeSliderData.stateMaxPrice = (this.rangeSliderData.stateMaxPrice <= this.rangeSliderData.stateMinPrice) ? this.rangeSliderData.stateMinPrice + 1: this.rangeSliderData.stateMaxPrice;
			},
			changeStateMaxPrice()
			{
				this.rangeSliderData.stateMaxPrice = (this.rangeSliderData.stateMinPrice >= this.rangeSliderData.stateMaxPrice) ? this.rangeSliderData.stateMinPrice + 1: this.rangeSliderData.stateMaxPrice;
			},
			changeStateMinPrice()
			{
				this.rangeSliderData.stateMinPrice = (this.rangeSliderData.stateMaxPrice <= this.rangeSliderData.stateMinPrice) ? this.rangeSliderData.stateMaxPrice - 1: this.rangeSliderData.stateMinPrice;
			},
			valideTest(e,statePrice)
			{
				let isLargerMaximum = (this.rangeSliderData[statePrice] >= this.maxValue),
					isEmpty = (this.rangeSliderData[statePrice] === ''),
					isLessZero = (this.rangeSliderData[statePrice] < 0);
				if(isLargerMaximum)
				{
					this.rangeSliderData[statePrice] = (statePrice === 'stateMinPrice')? this.maxValue - 1 : this.maxValue;
				};
				if(isEmpty || isLessZero)
				{
					this.rangeSliderData[statePrice] = 0;
				};
				/**
				* Удаление нуля в начале поля ввода(если он есть).
				*/
				if(e.target.value[0] == 0)
				{
					e.target.value = e.target.value.slice(1);
				};
				/**
				* Замена значения состояния максимальной цены на единицу, если оно равна нулю.
				*/
				if(statePrice === 'stateMaxPrice' && this.rangeSliderData[statePrice] === 0)
				{
					this.rangeSliderData[statePrice] = 1
				}
			},
		},
	};
</script>
<style lang="scss">
	.range-slider input[type="range"]
	{
		width: 100%;
		position:absolute;
		top:-5px;
		pointer-events: none;
		-webkit-appearance:none;
		z-index: 5;
		background: transparent;
		font-size: 14px;
		font-weight: 400;
		line-height: 20px;
	}
	.range-slider input[type="range"]::-webkit-slider-thumb
	{
		pointer-events:all;
		opacity: 0;
		cursor:pointer;
	}
	.range-slider__multi-range
	{
		position: relative;
		background-color: #FCF9EC;
		height: 5px;
		margin: 0 19px 0 16px;
	}
	.range-slider__thumb
	{
		position: absolute;
		width: 15px;
		height: 15px;
		border-radius: 50%;
		background-color:#FC4442;
		transform: translateY(-5px);
		cursor:pointer;
		z-index: 4;
	}
	.range-slider__difference-strip
	{
		pointer-events:none;
		position:absolute;
		height: 5px;
		background:#F0E19E;
		width: 100px;
		left: 25%;
		z-index: 3;
	}
	.range-slider__input-places
	{
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 16px;
		input
		{
			width: 47px;
			height: 40px;
			border: 1px solid #EAEAEA;
			border-radius: 5px;
			padding-left: 35px;
			font-size: 14px;
			line-height: 20px;
		}
	}
	.range-slider__input-place
	{
		height: 100%;
		position:relative;
		color:#2D2D2D;
		font-size: 14px;
		line-height: 20px;
		span
		{
			position:absolute;
			top:30%;
			left:15px;

		}
	}
	.range-slider__decoration
	{
		width: 12px;
		height: 2px;
		background:#EAEAEA;
		margin: 0 30px 0 29px;

	}
</style>