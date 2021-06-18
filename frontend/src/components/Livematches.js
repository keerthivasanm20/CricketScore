import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import CSRFToken from './csrftoken'


export default class Livematches extends Component {
    constructor(props) {
        super(props)
     
        this.state = {
             team1:1,
             team2:"",
             d:{'matches':[{}]},
        }
        this.getcurrentsong=this.getcurrentmatch.bind(this)
        this.getcurrentmatch();
       
        
    }
    
    getcurrentmatch()
    {
        
      
            fetch('/cric/matches/').then((response)=>
             response.json()
       ).then((data)=>{
         
        console.log(data);
       this.setState({
           d:data

       });
  
     
       });
     
    }
    render() {
      
        return (

            <div className="container">
            <Router> 
            <ul>
            {this.state.d.matches.map((item, i) => {
                      return  <li key={i}><form action='/cric/redirect/' method="POST"> <CSRFToken/><a><button className="but" type="submit"><h3>{item['team-1']} vs {item['team-2']} on {item['date']}</h3></button></a><input type="hidden" value={item['unique_id']} name="unique"/></form></li>
                    })}
            </ul>
            
            </Router> 
            </div>
        )
    }
}
