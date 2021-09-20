<template>
	<div class="subscribe-form">
		<h2 class="subscribe-form__title">Выгода с доставкой</h2>
		<p class="subscribe-form__abs">Подпишитесь и получайте промокоды, акции и подборки товаров на свою почту.</p>
		<ValidationObserver class="send-banner__form subscribe-form__form" v-slot="{handleSubmit}">
			<form @submit.stop.prevent="handleSubmit(sendForm)">
				<ValidationProvider name="required" rules="required|email" class="err" v-slot="{ errors }">
					<label class="send-banner__form-label subscribe-form__form-label">
						<input class="send-banner__form-input"
						type="text"
						placeholder="Введите e-mail"
						v-model="email"
						:class="{ 'success': !errors[0], 'error': errors[0] }"
						>
						<!-- v-model="phone" -->
						<button type="submit" class="btn subscribe-form__btn">Подписаться</button>
					</label>
					<span class="error-msg">{{ errors[0] }}</span>
				</ValidationProvider>
			</form>
		</ValidationObserver>
		<div class="subscribe-form__text">
			Нажимая «Подписаться» вы соглашаетесь с <NuxtLink to="#" class="subscribe-form__link">Условиями использования сайта</NuxtLink> и <NuxtLink to="#" class="subscribe-form__link">Политикой обработки персональных данных.</NuxtLink>
		</div>
	</div>
</template>
<style>
	.subscribe-form
	{
		background: #FCF9EC;
		border-radius: 20px;
		padding: 30px 15px 21px;
		text-align: center;
		color: #2D2D2D;
		margin-bottom: 29px;
	}
	h2.subscribe-form__title
	{
		font-weight: bold;
		font-size: 24px;
		line-height: 28px;
		margin: 0;
		margin-bottom: 15px;
	}
	.subscribe-form__abs
	{
		margin: 0;
		margin-bottom: 15px;
		font-weight: normal;
		font-size: 14px;
		line-height: 16px;
	}
	.subscribe-form__text
	{
		font-weight: normal;
		font-size: 12px;
		line-height: 18px;
	}
	.subscribe-form__link
	{
		text-decoration: underline;
		color: #2D2D2D;
	}
	.subscribe-form__form-label
	{
		position: relative;
		width: 100%;
		display: inline-block;
		margin-bottom: 15px;
	}
	.subscribe-form__form-label input
	{
		width: 100%;
	}
	.err{position: relative;}
	.error-msg
	{
		color:#FC4442;
		position: absolute;
		top: 30px;
		left: 50%;
		transform: translateX(-50%);
		width: 160px;
		transition:.2s;
	}
	.subscribe-form__form
	{
		margin-bottom: 15px;
	}
	@media (min-width: 768px)
	{
		.subscribe-form
		{
			padding-top: 25px;
			padding-bottom: 25px;
		}
		.subscribe-form__abs
		{
			font-size: 16px;
			line-height: 19px;
			margin-bottom: 49px;
		}
		.subscribe-form__form
		{
			max-width: 395px;
			margin: 0 auto;
			margin-bottom: 49px;
		}
		.subscribe-form__text
		{
			max-width: 400px;
			margin: 0 auto;
		}
		.subscribe-form__form-label{width: 516px;}
	}
</style>
<script>
	import {ValidationProvider,ValidationObserver} from 'vee-validate';
	import {extend} from 'vee-validate';
	import {required} from 'vee-validate/dist/rules';
	import {email} from 'vee-validate/dist/rules';
	extend('required',{
		...required,
		message:'Обязательное поле'
	})
	extend('email',{
		...email,
		message:'Некорректный email'
	})
	export default
	{
		data()
		{
			return{
				email:'',
			}
		},
		components:
		{
			ValidationProvider,
			ValidationObserver
		},
		methods:
		{
			sendForm(e)
			{
				console.log(true);
			},
		},
		mounted()
		{
		}
	}
</script>
