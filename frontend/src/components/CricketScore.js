import React from 'react'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import crci from '../cricket.png'
import ContentComponent from './ContentComponent';
import Livematches from './Livematches';
import Generalcomp from './Generalcomp';
import Searchcomponent from './Searchcomponent';
export default function CricketScore() {

    return (
        <div>
        <Router> 
        <nav class="jumbotron navbar navbar-expand-lg navbar-light bg-light" id="nav">
        <a class="navbar-brand" href="#"><h2>Cricscore<img  src={crci}></img></h2></a>

      
        <div  id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
             <Link to="/" class="nav-link" ><h3>Home<span className="glyphicon glyphicon-home"></span></h3> </Link>
            </li>
            <li class="nav-item active">
            <Link to="/" class="nav-link"><h3>About</h3> </Link>
          </li>
          <li class="nav-item active">
          <Link to="/live" class="nav-link" ><h3 >Live</h3></Link>
        </li>
        
          </ul>
          <form action="/cric/searchredirect/" method="GET" class="form-inline my-2 my-lg-0" id="search" >
            <input class="form-control mr-sm-2" name="team" type="search" placeholder="Search" aria-label="Search"/>
            <button class="btn btn-primary" type="submit">Search<span className="glyphicon glyphicon-search"></span></button>
          </form>
        </div>
      </nav>
      <div className="content">
          <switch>       
         
 <Route path="/score/:room" component={ContentComponent}></Route>
 <Route path="/results/:team" component={Searchcomponent}></Route>
 <Route exact path="/" component={Generalcomp}></Route>
 <Route path="/live" component={Livematches }>

 
</Route>

       
</switch> 
</div>
             </Router>
        </div>
    )
}
