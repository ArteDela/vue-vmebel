
<template>
	<div class="content">
		<SendBanner />
		<Catalog />
		<SubscribeForm />
	</div>
</template>

<script>
import SendBanner from '@/components/SendBanner'
import Catalog from '@/components/Catalog'
import SubscribeForm from '@/components/SubscribeForm'
import axios from 'axios'
export default
{
	components: { SendBanner, Catalog, SubscribeForm, },
	data()
	{
		return{
			info:null,
			res:[],
		}
	},
}
</script>