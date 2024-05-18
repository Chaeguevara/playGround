import { useRouter } from "next/dist/client/router";

function Greet(props){
    const {query} = useRouter();
    console.log(query)
    return(
        <h1>Hello, {query.name}!</h1>
    )
}
export default Greet;