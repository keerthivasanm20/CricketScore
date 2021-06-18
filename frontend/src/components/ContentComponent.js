import React, { Component } from 'react'

export default class ContentComponent extends Component {
     constructor(props) {
         super(props)
     
         this.state = {
              card:{}
         }
         this.id=this.props.match.params.room;
        
         this.getcurrentscore=this.getcurrentscore.bind(this);
         this.getcurrentscore();
     }
     componentDidMount()
    {
        this.interval=setInterval(this.getcurrentscore,1000)
    

    }
    componentWillUnmount()
    {
        clearInterval(this.interval);
    }
    getcurrentscore()
    {
        fetch('/cric/getscore'+'?code='+this.id)
        .then((response) =>{
            if(!response.ok){
                   return {};
            }
            else{
               return response.json();
            }
        }).then((data)=>{
           console.log(data)
            this.setState({
                  card:data,
               
            });
            
 
         
      
        });
         
     
  
    }
   
     
    render() {
        return (
            <div className="container" id="matchdet">
            {this.state.card.matchStarted ? 
                 <h3>{this.state.card.score}</h3> : <h3>OOPS...Notstarted         {this.state.card['team-1']} vs {this.state.card['team-2']}</h3>}
           
            </div>
        )
    }
}
