<template>
	<div class="send-banner">
		<div class="send-banner__left">
			<h2>Отправить заявку на добавление магазина</h2>
			<small>Подключение к макретплейсю бесплатное</small>
			<div class="send-banner__form">
				<input type="text" v-mask="'+7 (###) ###-##-##'" placeholder="+7" v-model="phone"/>
				<button>Отправить</button>
			</div>
		</div>
		<div class="send-banner__right">
			<img src="/images/sendbannerimg.png" alt="">
		</div>
	</div>
</template>
<script>
	export default
	{
		data()
		{
			return{
				phone:''
			}
		},
		components:
		{
		},
		methods:
		{
		},
		mounted()
		{
		}
	}
</script>
<style lang="scss">
	.send-banner
	{
		margin-bottom: 50px;
		background: #F5FBFB;
		margin-top: 36px;
		border-radius: 10px;
		display: flex;
		align-content: center;
		justify-content: center;
		padding:23px;
		overflow: hidden;
	}
	.send-banner__right{display: none;}
	.send-banner__left
	{
		small{display:none;}
		h2
		{
			color:#2D2D2D;
			font-size: 16px;
			margin:0px;
			font-weight:bold;
			margin-bottom: 7px;
			text-align: center;
		}
		small
		{
			color: #6C6C6C;
			font-size: 16px;
		}
	}
	.send-banner__form
	{
		position: relative;
		width:100%;
		margin-top:27px;
		input
		{
			border: 1px solid #EAEAEA;
			border-radius:100px;
			height:44px;
			padding:0 15px;
			width:100%;
			box-sizing: border-box;
		}
		button
		{
			position: absolute;
			background:#FC4442;
			border:0px;
			color:#fff;
			height:38px;
			padding:0 30px;
			border-radius: 50px;
			right:3px;
			top:3px;
			font-size: 13px;
		}
	}
	@media (min-width: 768px)
	{
		.send-banner
		{
			align-content: space-between;
			justify-content: space-between;
		}
		.send-banner__right{display: block;margin-right: 30px;}
		.send-banner__left small{display:block;}
		.send-banner__left h2{font-size: 26px;text-align: left;}
		.send-banner__form{max-width: 328px;}
	}
</style>