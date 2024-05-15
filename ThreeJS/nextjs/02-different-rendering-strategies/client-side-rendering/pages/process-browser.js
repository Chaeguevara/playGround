import styles from '../styles/Home.module.css';

function ProcessBrowserPage() {

  const side = process.browser ? 'client' : 'server'
  console.log(process.browser)
  return (
    <>
      <main className={styles.main}>
        <p> I'm running on the {side} </p>
      </main>
    </>
  );
}

export default ProcessBrowserPage;
