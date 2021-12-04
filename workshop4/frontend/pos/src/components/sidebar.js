
import icon1 from '../images/icon1.svg'
import icon2 from '../images/icon2.svg'
import icon3 from '../images/icon3.svg'
import icon4 from '../images/icon4.svg'
import icon5 from '../images/icon5.svg' 

function Sidebar() {
    return(
        <div className="flex flex-row w-auto flex-shrink-0 pl-4 pr-2 py-4">
            <div className="flex flex-col items-center py-4 flex-shrink-0 w-20 bg-cyan-500 rounded-3xl">
                <a className="flex items-center justify-center h-12 w-12 bg-cyan-50 text-cyan-700 rounded-full">  
                </a>
                <ul className="flex flex-col space-y-2 mt-12">
                <li>
                    <a href="#" className="flex items-center">
                    <span className="flex items-center justify-center h-12 w-12 rounded-2xl" >
                        <img src={icon1} />
                    </span>
                    </a>
                </li>
                <li>
                    <a href="#" className="flex items-center">
                    <span class="flex items-center justify-center text-cyan-100 hover:bg-cyan-400 h-12 w-12 rounded-2xl">
                        <img src={icon2} />
                    </span>
                    </a>
                </li>
                <li>
                    <a href="#" className="flex items-center">
                    <span class="flex items-center justify-center text-cyan-100 hover:bg-cyan-400 h-12 w-12 rounded-2xl">
                    <img src={icon3} />
                    </span>
                    </a>
                </li>
                <li>
                    <a href="#"
                    class="flex items-center">
                    <span class="flex items-center justify-center text-cyan-100 hover:bg-cyan-400 h-12 w-12 rounded-2xl">
                    <img src={icon4} />
                    </span>
                    </a>
                </li>
                </ul>
                <a> <img src={icon5} /> </a>
            </div>
            </div>
    )
}

export default Sidebar;