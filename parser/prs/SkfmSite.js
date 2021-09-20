/**
 * СКФМ
 * https://skfm-mebel.ru/
 */
class Skfm extends VMParser
{
	sections = [
		{
			url:'https://skfm-mebel.ru/product-category/perfecta/',
			vmebelSection:1,
			props:[
				{code:'collection',value:'Perfecta'}
			]
		},
		{
			url:'https://skfm-mebel.ru/product-category/divani/valensiya/',
			vmebelSection:1,
			props:[
				{code:'collection',value:'Валенсия'}
			]
		},
		{
			url:'https://skfm-mebel.ru/product-category/divani/rozalina/',
			vmebelSection:1,
			props:[
				{code:'collection',value:'Розалина'}
			]
		},
		{
			url:'https://skfm-mebel.ru/product-category/divani/sevilya/',
			vmebelSection:1,
			props:[
				{code:'collection',value:'Севилья'}
			]
		},
		{
			url:'https://skfm-mebel.ru/product-category/kuhni/',
			vmebelSection:2,
			props:[]
		},
		{
			url:'https://skfm-mebel.ru/product-category/gostinye/',
			vmebelSection:3,
			props:[]
		},
		{
			url:'https://skfm-mebel.ru/product-category/spalni/',
			vmebelSection:4,
			props:[]
		},
		{
			url:'https://skfm-mebel.ru/product-category/prihozhie/',
			vmebelSection:5,
			props:[]
		}
	];

	async getProducts(page)
	{
		for(let section in sections)
		{
			await page.goto(section.url);

			// парсим данные, сохраняме в БД
			let products = await page.$$('.product-type-simple');
			const hrefs1 = await page.evaluate( () => Array.from(
				document.querySelectorAll('.advice__box.advice__box--border'),
				el => {
					let product = new ProductDTO;
					product.pic   = el.querySelector('img').getAttribute('src');
					product.name  = el.querySelector('.advice__name').innerHTML;
					product.url   = el.querySelector('.advice__name').getAttribute('href');
					product.price = el.querySelector('.kitchen__price ').innerText.replace(/\D/g, '');

					return product;
				}
			));

		}
	}

}