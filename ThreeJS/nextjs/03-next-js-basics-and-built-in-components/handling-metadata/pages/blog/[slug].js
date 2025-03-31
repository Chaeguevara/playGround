import PostHead from '../../components/PostHead';
import posts from '../../data/posts';
import Image from "next/image"

//nextjs default api
export function getServerSideProps({ params }) {
  const { slug } = params;
  console.log(slug)
  const ee = posts.find((p) => p.slug === slug);

  return {
    props: {
      ee,
    },
  };
}

//prop name is dependant on `getServerSideProps`
function Post({ ee }) {
  return (
    <div>
      <PostHead {...ee} />
      <h1>{ee.title}</h1>
      <h2>{ee.subtitle}</h2>
      <p>{ee.subtitle}</p>
      <div style={{width:500,height:200,position:'relative'}}>
        <Image src={ee.image}
        layout='fill'
        objectFit='cover'
        alt={ee.title}
        />

      </div>
    </div>
  );
}

export default Post;
