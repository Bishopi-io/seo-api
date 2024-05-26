const axios = require('axios');

const url = 'https://api.bishopi.io/domain_seo_analysis/?domain=bishopi.io';

const headers = {
  'Authorization': 'Api-Key 1234'
};

axios.get(url, { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error making request:', error);
  });
