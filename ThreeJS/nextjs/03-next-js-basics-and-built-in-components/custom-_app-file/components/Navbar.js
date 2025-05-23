import { useContext } from 'react';
import Link from 'next/link';
import themeContext from './themeContext';

function Navbar() {
  const { toggleTheme, theme } = useContext(themeContext);
  const newThemeName = theme === 'dark' ? 'light' : 'dark';
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        marginBottom: 25,
      }}>
      <div>My Website</div>
      <div>
        <Link href="/">Home </Link>
        <Link href="/about-us">About </Link>
        <Link href="/contacts">Contacts </Link>
        <Link href="/posts">Posts</Link>
        <Link href={{
          pathname:'/[username]/[post]',
          query:{
            username:'chaeguevara',
            post:'helloworld',
          }
        }}>Read post</Link>
        <button onClick={toggleTheme}>Set {newThemeName} theme</button>
      </div>
    </div>
  );
}

export default Navbar;
