import React, { Component } from 'react'

export default class Generalcomp extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             card:{"det":['Loading please wait.....']}
        }
        this.getcurrentscore=this.getcurrentscore.bind(this);
       
    }
   
    componentDidMount()
    {
        this.getcurrentscore();
    

    }
    

  
   getcurrentscore()
   {  fetch('/cric/results/').then((response)=>
   response.json()
).then((data)=>{

console.log(data);
this.setState({
 card:data

});
           

        
     
       });
        
    
 
   }
  
    
    render() {
        return (
            <div class="container">
            <ul>
        {this.state.card.det.map((item, i) => {
          return <li key={i}><div class="jumbotron"><h4>{item}</h4></div></li>
        })}
      </ul>
            </div>
        )
    }
}
