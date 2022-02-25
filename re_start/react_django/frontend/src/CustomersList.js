import React, { Component } from 'react';

import CustomersService from './CustomersService';



const customersService = new CustomersService();


class CustomersList extends Component{ //  компонент CustomersList, расширяющий Component
   
   constructor(proprs){
      super(proprs); // Ключевое слово super используется для вызова функций, принадлежащих родителю объекта.
      this.state = { // иниц обьекта
         customers:[],
         nextPageURL: ''
      };
      this.nextPage = this.nextPage.bind(this); // выполняем привязку методов nextPage() и handleDelete(), this чтобы они были доступны из кода HTML.
      this.handleDelete = this.handleDelete.bind(this);
   }

   componentDidMount() { // ?
      // Метод componentDidMount() — это метод жизненного цикла компонента, вызываемый, когда компонент создается и вставляется в DOM.
      var self = this;
      customersService.getCustomer().then(function (result){
         //getCustomers() вызывает объект Customers Service для получения первой страницы данных и ссылки на следующую страницу из серверной части Django:
         self.setState({customers: result.data, nextPageURL:result.nextlink})
   
      });
      
   }

   handleDelete(e,pk) { // обрабатывает удаление клиента, под componentDidMount():
      var self = this;
      customersService.deleteCustomer({pk:pk}).then(() =>{ // удаления клиента по pk
         var newArr = self.state.customers.filter(function(obj){
            return obj.pk !== pk;
         });
         self.setState({customers: newArr})
      });
   }

   nextPage(){ // URL следующей страницы из объекта состояния this.state.nextPageURL 
      // и обновляет массив customers, добавляя в него возвращаемые данные.
      var self = this;
      customersService.getCustomersByURL(this.state.nextPageURL).then((result)=>{
         self.setState({ customers:result.date, nextPageURL: result.nextlink})
      });
   }

   render() {
      return (
         <div className='customers--list'>
            <table className='table'>
               <thead key='thead'>
                  <tr>
                     <th>#</th>
                     <th>First Name</th>
                     <th>Last Name</th>
                     <th>Phone</th>
                     <th>Email</th>
                     <th>Address</th>
                     <th>Description</th>
                     <th>Actions</th>
                  </tr>
               </thead>
               <tbody>
                  {this.state.customers.map(c=>
                     <tr key={c.pk}>
                        <td>{c.pk}</td>
                        <td>{c.first_name}</td>
                        <td>{c.last_name}</td>
                        <td>{c.phone}</td>
                        <td>{c.email}</td>
                        <td>{c.adress}</td>
                        <td>{c.description}</td>
                        <td>
                           <button onClick={(e)=> this.handleDelete(e,c.pk)}> Delete </button>
                           <a href={"/customer/"+ c.pk}> Update</a>
                        </td>
                     </tr>)}
               </tbody>
            </table>
            <button className='btn btn-primary' onClick={this.nextPage}>Next page</button> 
         </div>
      );
   }
}

export default CustomersList ;