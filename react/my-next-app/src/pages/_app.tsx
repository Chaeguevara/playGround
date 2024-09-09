import type { AppProps } from "next/app";

//global layout
export default function App({Component,pageProps}:AppProps){
    return <Component {...pageProps}/>
}