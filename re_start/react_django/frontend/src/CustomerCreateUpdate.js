import React, { Component } from "react";

import CustomersService from "./CustomersService";

const customersService = new CustomersService();


class CustomerCreateUpdate extends Component{
   constructor(props){
      super(props);
      this.handleSubmit=this.handleSubmit.bind(this); // привязка кнопок для возможность использованя их в форме
   }

   
   componentDidMount(){
      const{match:{params}} = this.props;
      if (params && params.pk){
         customersService.getCustomer(params.pk).then((c)=>{
            this.refs.firstName.value= c.first_name; // ?
            this.refs.lastName.value=c.last_name;
            this.refs.email.value=c.email;
            this.refs.phone.value=c.phone;
            this.refs.address.value=c.address;
            this.refs.description.value=c.description;
         })
      }
   }


   handelCreate(){ // создание клиента на основе введённых данных
      //Он вызывает соответствующий метод CustomersService.createCustomer()
      customersService.createCustomer({ // , который API использует для вызова серверной части для создания клиента.
         'first_name': this.refs.firstName.value,
         'last_name': this.refs.lastName.value,
         'email': this.refs.email.value,
         'phone': this.refs.phone.value,
         'address': this.refs.address.value,
         'description': this.refs.description.value,
      }).then((result)=>{alert('Customer created!')}).catch(()=>{
         alert('There was an eroor! Please re-check your datas')
      })
   }


   handleUpdate(pk){ //  обновляет клиента по pk, используя новую информацию из формы данных о клиенте.
      customersService.updateCustomer({
         'first_name': this.refs.firstName.value,
         'last_name': this.refs.lastName.value,
         'email': this.refs.email.value,
         'phone': this.refs.phone.value,
         'address': this.refs.address.value,
         'description': this.refs.description.value,
      }).then((result)=>{alert('Customer updated')}).catch(()=>{
         alert('Customer update Error');
      });
   }

   
   handleSubmit(event){
      const{match:{params}} = this.props;
      if (params && params.pk){ // if .. => upd
         this.handleUpdate(params.pk);
      }else{ this.handelCreate() } // else create
      event.preventDefault();
   }
   render(){
      return( //Для каждого элемента ввода формы метод добавляет свойство ref для доступа и установки значения элемента формы.

         <form onSubmit={this.handleSubmit}>
            <div className="form-group">
               <label>First Name :</label>
               <input className="form-control" type="text" ref='firstName'></input>

               <label>Last Name :</label>
               <input className="form-control" type="text" ref='lastName'></input>

               <label>Phone :</label>
               <input className="form-control" type="text" ref='phone'></input>

               <label>Email :</label>
               <input className="form-control" type="text" ref='email'></input>

               <label>Adress :</label>
               <input className="form-control" type="text" ref='adress'></input>

               <label>Description :</label>
               <textarea className="form-control" ref='description'></textarea>

               <input className="btn btn-primary" type="submit" value="Submit"></input>

            </div>
         </form>
      );
    }

}

export default CustomerCreateUpdate;