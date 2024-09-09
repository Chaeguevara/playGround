import { Html, Head, Main, NextScript } from 'next/document'

//custom document file https://nextjs.org/docs/pages/building-your-application/routing/custom-document
export default function Document() {
    return (
        <Html>
            <Head />
            <body>
                <Main />
                <NextScript />
            </body>
        </Html>
    )
}