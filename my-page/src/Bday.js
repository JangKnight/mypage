import styles from "./Bday.module.css";

const Bday = (props) => {
  return (
    <article className={styles.container}>
      <h2>{props.name}</h2>
      <p>{props.birthday}</p>
    </article>
  );
};

export default Bday;
