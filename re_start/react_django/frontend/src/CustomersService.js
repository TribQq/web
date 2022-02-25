import axios from 'axios'
const API_URL = 'http://localhost:8000'



export default class CustomersService{

   constructor(){}
   

   getCustomers(){ //  получает первую страницу клиентов.
      const url = `${API_URL}/api/customres`;
      return axios.get(url).then(response => response.data);
   }

   getCustomersByURL(link){ // получает клиентов по URL. Это позволяет получить следующие страницы клиентов путем передачи таких ссылок, как /api/customers/?page=2.
      const url = `${API_URL}${link}`;
      return axios.get(url).then(response => response.data);
   }

   getCustomer(pk){ //  получает клиента по первичному ключу.
      const url = `${API_URL}/api/customers/${pk}`;
      return axios.get(url).then(response => response.data);
   }
   
   deleteCustomer(customer){ //  удаляет клиента.
      const url = `${API_URL}/api/customers/${customer.pk}`;
      return axios.delete(url);
   }

   createCustomer(customer){ //  создает клиента.
      const url = `${API_URL}/api/customers/`;
      return axios.post(url, customer);
   }

   updateCustomer(customer){  // upd   клиента.
      const url = `${API_URL}/api/customers/${customer.pk}`;
      return axios.put(url, customer);
   }
}