import axios from 'axios';
export const state = () => ({
	catalogs: []
});

export const mutations =
{
	setCatalogFromState:(state,catalogs)=>
	{
		state.catalogs = catalogs;
	}
};

export const actions =
{
	getCatalogs({commit})
	{
		return axios('http://5.53.124.137/categories',{
			method:'GET',
		}).then((catalogs)=>
		{
			commit('setCatalogFromState',catalogs.data);
			return catalogs;
		});
	}
};

export const getters =
{
	catalogs(state)
	{
		return state.catalogs;
	},
};