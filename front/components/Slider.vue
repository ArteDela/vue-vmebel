<template>
	<div class="slider">
		<div class="slider__main-place">
			<ul v-bind:style="{ 'right':(stateSlider*100)+'%'}">
				<li v-for="imgUrl of images">
					<img :src="imgUrl">
				</li>
			</ul>
			<button class="slider__button-left" @click="switchPageLeftMobile()">
				<svg-icon name="Arrow-left-white" height="15" width="15"/>
			</button>
			<button class="slider__button-right" @click="switchPageRightMobile()">
				<svg-icon name="Arrow-right-white" height="15" width="15"/>
			</button>
		</div>
		<div class="slider__controllers">
			<ul class="slider__mini-pages-list"v-bind:style="{ 'right': ((isDesktop) ? stateMiniSlider*156 : stateMiniSlider*149)+'px'}">
				<li
					v-for="(item, index) of images"
					@click="stateSlider = index"
					:class="{'slider__controllers-active' : (stateSlider === index)}">
					<img :src="item">
				</li>
			</ul>
			<button class="slider__button-right" @click="switchPageRight()">
				<svg-icon name="Arrow-right-white"  height="15" width="15"/>
			</button>
			<button class="slider__button-left" @click="switchPageLeft()">
				<svg-icon name="Arrow-left-white"  height="15" width="15"/>
			</button>
		</div>
	</div>
</template>
<script>
	export default
	{
		props:{ images:Array},
		data(){
			return{
				isDesktop:false,
				stateSlider:2,
				stateMiniSlider:0,
			};
		},
		mounted() {
			this.onResize()
			window.addEventListener('resize', this.onResize)
		},
		methods:{
			onResize() {
				this.isDesktop = window.innerWidth > 1200;
			},
			switchPageRight()
			{
				this.stateMiniSlider += ( this.stateMiniSlider < this.images.length-5 &&  this.stateSlider > 1) ? 1 : (this.stateSlider === this.images.length-1) ? - this.stateMiniSlider: 0;
				this.stateSlider += (this.stateSlider < this.images.length-1)? 1 : -this.stateSlider;

			},
			switchPageLeft()
			{
				this.stateMiniSlider -= (this.stateMiniSlider > 0 && this.stateSlider < this.images.length-2) ? 1 : (this.stateSlider === 0) ? -this.images.length + 5 : 0;
				this.stateSlider -= (this.stateSlider > 0 )? 1 : -this.images.length + 1;
			},
			switchPageRightMobile()
			{
				this.stateSlider += (this.stateSlider < this.images.length-1)? 1 : -this.stateSlider;
			},
			switchPageLeftMobile()
			{
				this.stateSlider -= (this.stateSlider > 0 )? 1 : -this.images.length + 1;
			}
		},
	};
</script>
<style lang="scss" scoped>
	.slider__main-place
	{
		margin-bottom: 10px;
		overflow: hidden;
		ul{ padding: 0;}
		img{ height: 201px;}
	}
	.slider
	{
		margin:0 auto;
		position: relative;
		min-width: 335px;
		max-width: 351px;
		margin-bottom: 10px;
	}
	.slider ul
	{
		position:relative;
		padding: 0;
		margin: 0;
		list-style: none;
		white-space: nowrap;
		transition:all .3s ease;
	}
	.slider li
	{
		display: inline-block;
		width: 100%;
	}
	.slider button
	{
		display: none;
		position: absolute;
		top: 33%;
		padding-top: 6px;
		height: 31.81px;
		width: 31.73px;
		border: none;
		border-radius: 50%;
		color: white;
		background: #2D2D2D;
	}
	.slider__main-place img
	{
		display: block;
		margin:0 auto;
		width: 100%;
		object-fit: cover;
	}
	.slider:hover .slider__main-place > button{ display: block;}
	.slider button svg
	{
		width: 18px;
		height: 18px;
	}
	.slider__button-left{ left: 0;}
	.slider__button-right{ right: 0;}
	.slider__controllers
	{
		text-align: center;
		height: 40px;
		ul
		{
			padding: 0;
			text-decoration: none;
			margin: 0;
			transition:all .3s ease;
		}
		li
		{
			display: inline-block;
			height: 8px;
			width: 8px;
			background-color: #2D2D2D;
			border-radius: 50%;
			margin: 0;
			margin-right: 11px;
			max-width: 138px;
			max-height: 87px;
			&:last-child{ margin: 0;}
		}
		button{ display: none;}
		.slider__controllers-active{ background-color: #CCCCCC;}
		img
		{
			display: none;
			object-fit: cover;
    		width: 100%;
    	}
	}
	@media (min-width: 768px)
	{
		.slider
		{
			margin: 0 auto;
			margin-bottom: 40px;
			width: 728px;
			max-width: unset;
		}
		.slider__main-place > button { display: none;}
		.slider__main-place
		{
			height: 419px;
			img{ height: 419px;}
		}
		.slider__controllers
		{
			position: relative;
			width: 100%;
			overflow: hidden;
			white-space: nowrap;
			height: max-content;
			li
			{
				width: 129px;
				height: 100%;
				background-color: unset;
				border-radius: 4px;
				margin: 0;
			}
			img
			{
				height: 100%;
				display: inline-block;
				border-radius: 4px;
				object-fit: cover;
    			width: 100%;
			}
			button
			{
				display: block;
				top:30%;
			}
			.slider__controllers-active
			{
				background-color: unset;
				position: relative;
			}
			.slider__controllers-active::after
			{
				content:'';
				position: absolute;
				top:0;
				left:0;
				height: 100%;
				width: 100%;
				box-shadow: inset 0 0 0 2px #2D2D2D;
				border-radius: 4px;
			}
		}
		.slider__mini-pages-list
		{
			display: grid;
			grid-template-columns:129px;
			grid-template-rows: 87px;
			grid-auto-flow: column;
			grid-gap:20px;
			white-space:nowrap;
			width: max-content;
			height: 100%;
		}
		.slider__button-left{ left: 9px;}
		.slider__button-right{ right: 9px;}
		.slider:hover .slider__main-place > button{ display: none;}
	}
	@media (min-width: 1440px)
	{
		.slider
		{
			margin: 0;
			margin-right: 21px;
			width: 776px;
		}
		.slider__controllers li img{ display: inline-block;}
		.slider__main-place
		{
			height: 419px;
			margin-bottom: 13px;
			img{ height: 419px;}
		}
		.slider__mini-pages-list
		{
			grid-template-columns:138px;
			grid-gap:22px;
		}
	}
</style>
