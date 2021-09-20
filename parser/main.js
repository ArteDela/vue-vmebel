const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch({
		headless:true,
		args: ['--no-sandbox']
	});
	const page = await browser.newPage();
	await page.goto('https://skfm-mebel.ru/product-category/perfecta/');

	// парсим данные, сохраняме в БД
	let products = await page.$$('.product-type-simple');
	const hrefs1 = await page.evaluate( () => Array.from(
		document.querySelectorAll('.advice__box.advice__box--border'),
		el => {
			return {
				pic: el.querySelector('img').getAttribute('src'),
				name: el.querySelector('.advice__name').innerHTML,
				url: el.querySelector('.advice__name').getAttribute('href'),
				price: el.querySelector('.kitchen__price ').innerText.replace(/\D/g, ''),
			}
		}
	));

	console.log(hrefs1);

	await browser.close();

})();