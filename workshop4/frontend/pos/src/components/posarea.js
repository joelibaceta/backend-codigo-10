import React, { useEffect, useRef } from 'react'
import axios from "axios"
import EmptyIcon from '../images/empty.svg' 
import Cart from './cart'

function PosArea() {

    const [productList, setProductList] = React.useState([])
    const cartRef = useRef();

    function getProducts(){
        axios.get("http://localhost:5000/products")
            .then((res) => {
                console.log(res.data)
                setProductList(res.data)
                cartRef.current.refresh()
            })
            .catch((err) => {
                console.log(err)
            })
        
    }

    function isEmpty(){
        return (productList.length === 0)
    }

    useEffect(() => {
        getProducts()
    }, [])

    return (
        <div class="flex-grow flex">
            <div class="flex flex-col bg-blue-gray-50 h-full w-full py-4">
                    <div class="flex px-2 flex-row relative">
                    <div class="absolute left-5 top-3 px-2 py-2 rounded-full bg-cyan-500 text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </div>
                    <input
                        type="text"
                        class="bg-white rounded-3xl shadow text-lg full w-full h-16 py-4 pl-16 transition-shadow focus:shadow-2xl focus:outline-none"
                        placeholder="Cari menu ..."
                    />
                    </div>
                    <div class="h-full overflow-hidden mt-4">
                    <div class="h-full overflow-y-auto px-2">
                        { isEmpty() ? (
                            <div class="select-none bg-blue-gray-100 rounded-3xl flex flex-wrap content-center justify-center h-full opacity-25">
                                <div class="w-full text-center">
                                    <center>
                                    <img src={EmptyIcon} width="100px"/>
                                    </center>
                                    <p class="text-xl">
                                    YOU DON'T HAVE
                                    <br/>
                                    ANY PRODUCTS TO SHOW
                                    </p>
                                </div>
                            </div>
                        ) : (
                            <div   class="grid grid-cols-4 gap-4 pb-3">
                                {productList.map((product) => {
                                    return(
                                        <div 
                                            className="select-none cursor-pointer transition-shadow overflow-hidden rounded-2xl bg-white shadow hover:shadow-lg"
                                            onClick={e => {cartRef.current.addProductToCart(product)}}
                                        >
                                            <img src={product.picture} />
                                            <div class="flex pb-3 px-3 text-sm -mt-3">
                                                <p class="flex-grow truncate mr-1">{product.name}</p>
                                                <p class="nowrap font-semibold">{product.price}</p>
                                            </div>
                                        </div>
                                    )
                                } )}
                            </div>
                        )}
                        
                         
                        
                    </div>
                    </div>
            </div>
            <Cart ref={cartRef}></Cart>
        </div>
    )
}

export default PosArea;