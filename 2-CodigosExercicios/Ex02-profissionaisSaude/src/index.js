import React from 'react'
import ReactDOM from 'react-dom'
import './styles.css'
import img1 from './images/img1.jpeg'

const App = () => {
    const style_cnt_main = () => {
        return {width: 1280, margin: 'auto', border: '1px solid black', backgroundColor: "#EEE", borderRadius: 8, padding: 12,
        textAlign: 'center'}
    };

    const doctorNames = {doc1: "Maria", doc2: "Joao", doc3: "Gabriela"}

    return <div style={style_cnt_main()}>
            <h2>Profissionais de saúde</h2>
                <div style={{margin: 8, border: '1px solid #DDD', borderRadius: 8, padding: 8, display: 'flex', flexDirection: 'row', justifyContent: 'space-around'}}> 
                    <div className='doctor'>
                        <img src={img1} />
                        <p>{doctorNames.doc1}</p>
                    </div>

                    <div className='doctor'>
                        <img src={process.env.PUBLIC_URL+'img2.jpg'} />
                        <p>{doctorNames.doc2}</p>
                    </div>

                    <div className='doctor'>
                        <img src="https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg"/>
                        <p>{doctorNames.doc3}</p>
                    </div>
                    
                </div> 
        </div>
}

ReactDOM.render(
    <App/>,
    document.querySelector("#root")
)

