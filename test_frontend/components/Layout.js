import Nav from './Nav'
import Head from 'next/head'

const Layout = (props) => {
    return (
        <>
            <Head>
                <title>Currency Application</title>
                <link rel="icon" href="https://cdn3.iconfinder.com/data/icons/hotel-10-1/48/452-512.png"></link>
            </Head>
            <div>
                <Nav/>
                {props.children}
            </div>
        </>
    )
}

export default Layout