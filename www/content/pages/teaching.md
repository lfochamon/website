Title: Teaching
Date: 1002-01-03
status: hidden

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<style>
  .carousel {
    position: relative;
  }

  .carousel-inner {
    position: relative;
    width: 100%;
    overflow: hidden;
  }

  .carousel-item {
    position: relative;
    display: none;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    width: 100%;
    height: 150px;
    transition: -webkit-transform 0.6s ease;
    transition: transform 0.6s ease;
    transition: transform 0.6s ease, -webkit-transform 0.6s ease;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    perspective: 1000px;
  }

  @media (min-width: 48em) {
    .carousel-item {
      height: 120px;
    }
  }

  .carousel-item.active,
  .carousel-item-next,
  .carousel-item-prev {
    display: block;
  }

  .carousel-item-next,
  .carousel-item-prev {
    position: absolute;
    top: 0;
  }

  .carousel-item-next.carousel-item-left,
  .carousel-item-prev.carousel-item-right {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }

  @supports ((-webkit-transform-style: preserve-3d) or (transform-style: preserve-3d)) {
    .carousel-item-next.carousel-item-left,
    .carousel-item-prev.carousel-item-right {
      -webkit-transform: translate3d(0, 0, 0);
      transform: translate3d(0, 0, 0);
    }
  }

  .carousel-item-next,
  .active.carousel-item-right {
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }

  @supports ((-webkit-transform-style: preserve-3d) or (transform-style: preserve-3d)) {
    .carousel-item-next,
    .active.carousel-item-right {
      -webkit-transform: translate3d(100%, 0, 0);
      transform: translate3d(100%, 0, 0);
    }
  }

  .carousel-item-prev,
  .active.carousel-item-left {
    -webkit-transform: translateX(-100%);
    transform: translateX(-100%);
  }

  @supports ((-webkit-transform-style: preserve-3d) or (transform-style: preserve-3d)) {
    .carousel-item-prev,
    .active.carousel-item-left {
      -webkit-transform: translate3d(-100%, 0, 0);
      transform: translate3d(-100%, 0, 0);
    }
  }

  .carousel-control-prev,
  .carousel-control-next {
    position: absolute;
    top: 0;
    bottom: 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    width: 15%;
    color: #fff;
    text-align: center;
    opacity: 0.5;
  }

  .carousel-control-prev:hover, .carousel-control-prev:focus,
  .carousel-control-next:hover,
  .carousel-control-next:focus {
    color: #fff;
    text-decoration: none;
    outline: 0;
    opacity: .9;
  }

  .carousel-control-prev {
    left: 0;
  }

  .carousel-control-next {
    right: 0;
  }

  .carousel-control-prev-icon,
  .carousel-control-next-icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    background: transparent no-repeat center center;
    background-size: 100% 100%;
  }

  .carousel-control-prev-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
  }

  .carousel-control-next-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
  }

  .carousel-indicators {
    position: absolute;
    right: 0;
    top: 0;
    bottom: 10px;
    left: 0;
    z-index: 15;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    padding-left: 0;
    margin-right: 15%;
    margin-left: 15%;
    list-style: none;
  }

  .carousel-indicators li {
    background-color: #ddd;
    position: relative;
    -webkit-box-flex: 0;
    -ms-flex: 0 1 auto;
    flex: 0 1 auto;
    width: 30px;
    height: 5px;
    margin-right: 3px;
    margin-left: 3px;
    text-indent: -999px;
  }

  .carousel-indicators li::before {
    position: absolute;
    top: -10px;
    left: 0;
    display: inline-block;
    width: 100%;
    height: 10px;
    content: "";
  }

  .carousel-indicators li::after {
    position: absolute;
    bottom: -10px;
    left: 0;
    display: inline-block;
    width: 100%;
    height: 10px;
    content: "";
  }

  .carousel-indicators .active {
    background-color: #0a5daa;
  }

  .carousel-caption {
    position: absolute;
    right: 15%;
    bottom: 20px;
    left: 15%;
    z-index: 10;
    padding-top: 20px;
    padding-bottom: 20px;
    color: #fff;
    text-align: center;
  }

  .carousel-item p:first-of-type {
    margin-top: 1rem;
  }

</style>

# Teaching

&nbsp;

<div id="teachingQuotes" class="carousel slide" data-ride="carousel" data-interval="8000">
  <div class="carousel-inner">
    <div class="carousel-item active">
    <p>"Thanks for everything you did for us this summer! Your guidance and humor definitely made the experience even better."</p>
    <p style="line-height:100%;">Carly Staebell<br />
    <span style="font-size:75%;">Summer Undergraduate Fellowship in Sensor Technologies (SUNFEST), 2018</span></p>
    </div>
    <div class="carousel-item">
    <p>"I thought that Luiz gave an awesome lecture today.  We were pleasantly surprised, usually TAs are not that good / skilled."</p>
    <p style="line-height:100%;">Robert Mack Pierson<br />
    <span style="font-size:75%;">Stochastic Systems Analysis and Simulation (ESE 303), 2017</span></p>
    </div>
    <div class="carousel-item">
    <p>"I’m in ESE 224 and really enjoyed your lecture this morning."</p>
    <p style="line-height:100%;">Jacob Bendell<br />
    <span style="font-size:75%;">Signal and Information Processing (ESE 224), 2020</span></p>
    </div>

    <ol class="carousel-indicators">
      <li data-target="#teachingQuotes" data-slide-to="0" class="active"></li>
      <li data-target="#teachingQuotes" data-slide-to="1"></li>
      <li data-target="#teachingQuotes" data-slide-to="2"></li>
    </ol>
  </div>

</div>

&nbsp;

## Experience

- **2009**: Instructor for non-destructive testing certification course at INSACAST, France  
- **2013&ndash;2014**: TA for undergraduate probability at the University of São Paulo, Brazil  
- **2016&ndash;2019**: TA for undergraduate probability at the University of Pennsylvania, USA
- **2017&ndash;2020**: TA for undergraduate signal processing (*in person and virtual*) at the University of Pennsylvania, USA
- **2018&ndash;2019**: Research mentor of [SUNFEST](https://sunfest.seas.upenn.edu/) (NSF-sponsored REU program at Penn)
- \> 7 years mentoring undergraduate and graduate research

&nbsp;

## Instructional videos

As a TA for undergraduate probability back in Brazil, I produced a series of
instructional videos to complement or further explain parts of the material
seen in class. The goal of these videos was not only to provide more detailed derivations
than those presented in class, for instance, proving the central limit theorem or
showing how to compute the integral of the Gaussian distribution, but also to give
more conceptual explanations, such as the difference between independent and disjoint
events. I also took this opportunity to give a bit of historical context to the
topics, telling the story of the development of the central limit theorem or how
the Gaussian distribution came to be called "Gaussian." Additionally, I explored
philosophical aspects of probability that are rarely covered in mathematical
probability courses, such as "What is a probability?"

These videos are available on [YouTube](https://www.youtube.com/user/luizchamon/videos)
(in Portuguese) and have received over *130.000 views*.


<div style="float:left; margin-right:1rem;">
  <iframe width="250" height="160" src="https://www.youtube.com/embed/v0GRhhfxwkM" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div style="float:left; margin-right:1rem;">
  <iframe width="250" height="160" src="https://www.youtube.com/embed/vyHSG58FCyk" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div style="float:left; margin-right:1rem;">
  <iframe width="250" height="160" src="https://www.youtube.com/embed/Z27iTuLhkG4" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div style="clear:both;"></div>


&nbsp;

## Recording

As part of my certification through Penn's [Center for Teaching and Learning](https://www.ctl.upenn.edu/),
I had one of my live classes recorded. It's a good watch if (and probably ONLY IF) you're interested in learning
about the use of continuous-time Markov chains to simulate chemical reactions and how bacteria in our intestines digest milk.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BjS3FeXrOWE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
