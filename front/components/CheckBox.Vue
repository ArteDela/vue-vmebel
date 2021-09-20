<template>
	<div class="checkbox">
		<input
			type="checkbox"
			:id="id"
			:checked="state"
			@change="$emit('changeState')"
		>
		<label
			:for="id"
			class="checkbox__point"><svg-icon name="checked-icon"
		>
			</svg-icon>
		</label>
		<label :for="id" class="checkbox__label">{{label}}</label>
	</div>
</template>
<script>
	export default
	{
		props:
		{
			label:String,
			id:String,
			state:Boolean,
		},
	};
</script>
<style lang="scss" scoped>
	.checkbox
	{
		position: relative;
		user-select: none;
		input
		{
			position:absolute;
			opacity: 0;
			height: 0;
			width: 0;
		}
		input:checked + .checkbox__point
		{
			background: #F0E19E;
			svg	{ opacity: 1;}
		}
	}
	.checkbox__point
	{
		display: block;
		position: relative;
		float:left;
		padding: 0;
		margin: 0 10px 0 0;
		cursor: pointer;
		border-radius: 3px;
		height: 20px;
		width: 20px;
		& > svg
		{
			opacity: 0;
			width: 11px;
			height: 10px;
			position: absolute;
			left:25%;
			top:25%;
		}
	}
	.checkbox__label
	{
		vertical-align: top;
		cursor: pointer;
		color:#6C6C6C;
		font-size: 14px;
		font-weight: 400;
		line-height: 20px;
	}
</style>