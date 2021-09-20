<template>
	<div class="check-box-list">
		<div class="check-box-list__find-place">
			<input
				type="text"
				placeholder="Найти"
				v-model="findName"
			>
			<svg-icon name="shape" />
		</div>
		<main>
			<div
				class="check-box-list__checkbox"
				v-for="(item, index) of checkBoxListData"
				:key="index"
			>
				<CheckBox
					v-if="existFindNameInLabelName(item)"
					:label="item.name"
					:id="id + index"
					:state="item.state"
					@changeState="item.state = !item.state"
				/>
			</div>
		</main>
	</div>
</template>
<script>
	import CheckBox from '@/components/CheckBox';
	export default
	{
		name:"check-box-list",
		components:
		{
			CheckBox,
		},
		props:
		{
			id:String,
			checkBoxListData:Array,
		},
		data()
		{
			return {
				findName:'',
			};
		},
		methods:
		{
			existFindNameInLabelName(checkBox)
			{
				return checkBox.name.toUpperCase().includes(this.findName.toUpperCase())
			},
		},
	};
</script>
<style lang="scss">
	.check-box-list__find-place
	{
		position: relative;
		width: min-content;
		svg
		{
			position: absolute;
			right: 12px;
			top:32%;
			height: 16px;
			width: 16px;
		}
		input
		{
			margin-bottom: 12px;
			padding-left: 12px;
			display: block;
			border:1px solid #EAEAEA;
			border-radius: 5px;
			min-width: 225px;
			height: 40px;
			font-size: 14px;
		}
		input::placeholder
		{
			color:#6C6C6C;
			font-weight: 400;
		}
	}
	.check-box-list__checkbox{margin-bottom: 15px;}
	.check-box-list main
	{
		max-height: 246px;
		overflow: auto;
	}
</style>