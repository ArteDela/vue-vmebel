export default {
	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		title: 'Мебель Владикавказ',
		htmlAttrs: {
			lang: 'en'
		},
		meta: [
			{ charset: 'utf-8' },
			{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
			{ hid: 'description', name: 'description', content: '' }
		],
		link: [
			{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
		]
	},

	// Global CSS: https://go.nuxtjs.dev/config-css
	css: [
		'@/static/fonts/roboto.css',
		'~/assets/normalize.css'
	],

	// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
	plugins: [
		'@/plugins/directives',
		'@/plugins/v-mask',
		'@/plugins/validator',
		// { src: '@/plugins/ymapPlugin.js',  mode: 'client' },
		// { src: '~plugins/validator', ssr: false }
	],

	// Auto import components: https://go.nuxtjs.dev/config-components
	components: true,

	// Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
	buildModules: [
		'@nuxtjs/svg-sprite',
	],

	// Modules: https://go.nuxtjs.dev/config-modules
	modules: [
		['vue-yandex-maps/nuxt', { apiKey: 'xxx',lang: 'ru_RU',version: '2.1',} ],
	],

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {
		transpile: ["vee-validate/dist/rules"],
		extend(config, ctx){}
	}
};
