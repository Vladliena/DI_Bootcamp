import logo from './logo.svg';
import './App.css';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';

function App() {
  return (
    <div style={{ width: '400px' }}>
        <Carousel>
          <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg" />
            <p className="legend">Hong Kong</p>
          </div>
          <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp" />
            <p className="legend">Macao</p>
          </div>
          <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp" />
            <p className="legend">Japan</p>
          </div>
        </Carousel>
    </div>
  );
}

export default App;
