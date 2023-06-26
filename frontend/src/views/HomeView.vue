<script setup>
import { ref } from 'vue'
import Button from '../components/DynamicButton.vue'
import TrainingCard from '../components/TrainingCard.vue'
import TrainingModal from '../components/TrainingModal.vue'

const trainings = [
  {
    id: 1,
    level: 'Beginner',
    description:
      'Learn the fundamentals of the game. Learn the rules and basic skills like passing and dribbling and shooting',
    cta: 'Start Learning',
    background:
      'https://ik.imagekit.io/Ochoja01/Mamba_Mentality/traning.png?updatedAt=1687380866894'
  },
  {
    id: 2,
    level: 'Intermediate',
    description:
      'Improve upon basic skills. Gain better understanding of the game. Take skills to the next level.',
    cta: 'Improve My Game',
    background:
      'https://ik.imagekit.io/Ochoja01/Mamba_Mentality/training2.png?updatedAt=1687380869575'
  },
  {
    id: 3,
    level: 'Advanced',
    description:
      'Develop deep understanding of the game. Perfect your skills to compete professionally.',
    cta: 'Master My Craft',
    background:
      'https://ik.imagekit.io/Ochoja01/Mamba_Mentality/training3.png?updatedAt=1687380869141'
  }
]

const openModal = ref(false)

const closePopup = () => (openModal.value = false)
</script>

<template>
  <Teleport to="body" v-if="openModal">
    <TrainingModal @closeModal="closePopup"></TrainingModal>
  </Teleport>

  <header>
    <div class="text">
      <h1 class="slogan">Never let good enough <span class="green">be</span> enough!</h1>
      <div class="caption">Curated videos and materials to take your game to the next level</div>

      <Button @click="openModal = true">Improve My Game</Button>
    </div>
  </header>

  <section class="training">
    <h2>Best Training For You</h2>
    <div class="cards">
      <TrainingCard
        v-for="training in trainings"
        :level="training.level"
        :description="training.description"
        :cta="training.cta"
        :key="training.id"
        :background="training.background"
      >
      </TrainingCard>
    </div>
  </section>

  <section class="how-tos">
    <h2>How Tos</h2>

    <div class="category">
      <div class="active">Articles</div>
      <div>Videos</div>
    </div>

    <div class="articles">
      <div class="post">
        <div class="img">
          <img
            src="https://ik.imagekit.io/Ochoja01/Mamba_Mentality/blogimg.png?updatedAt=1687385606459"
            alt=""
          />
        </div>
        <div class="title">The Art of Shooting - How to shoot the rock</div>
        <div class="snippet">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maiores, blanditiis nemo cum
          doloremque...
        </div>

        <div class="publisher">
          <div class="author-img">
            <img
              src="https://ik.imagekit.io/Ochoja01/Mamba_Mentality/faceimg.png?updatedAt=1687387303755"
              alt=""
            />
          </div>
          <div class="author">
            <div class="name">Ash Steve</div>
            <div class="date">24th September, 2023</div>
          </div>
        </div>
      </div>

      <div class="post">
        <div class="img">
          <img
            src="https://ik.imagekit.io/Ochoja01/Mamba_Mentality/blogimg.png?updatedAt=1687385606459"
            alt=""
          />
        </div>
        <div class="title">The Art of Shooting - How to shoot the rock</div>
        <div class="snippet">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maiores, blanditiis nemo cum
          doloremque...
        </div>

        <div class="publisher">
          <div class="author-img">
            <img
              src="https://ik.imagekit.io/Ochoja01/Mamba_Mentality/faceimg.png?updatedAt=1687387303755"
              alt=""
            />
          </div>
          <div class="author">
            <div class="name">Ash Steve</div>
            <div class="date">24th September, 2023</div>
          </div>
        </div>
      </div>

      <div class="post">
        <div class="img">
          <img
            src="https://ik.imagekit.io/Ochoja01/Mamba_Mentality/blogimg.png?updatedAt=1687385606459"
            alt=""
          />
        </div>
        <div class="title">The Art of Shooting - How to shoot the rock</div>
        <div class="snippet">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maiores, blanditiis nemo cum
          doloremque...
        </div>

        <div class="publisher">
          <div class="author-img">
            <img
              src="https://ik.imagekit.io/Ochoja01/Mamba_Mentality/faceimg.png?updatedAt=1687387303755"
              alt=""
            />
          </div>
          <div class="author">
            <div class="name">Ash Steve</div>
            <div class="date">24th September, 2023</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
header {
  height: 65vh;
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
    url(https://ik.imagekit.io/Ochoja01/Mamba_Mentality/hero.png?updatedAt=1687364216670);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;

  .text {
    color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80%;
    width: 90%;
    margin: auto;
    text-align: center;

    .slogan {
      font-size: 4em;
      font-weight: 700;
      margin-bottom: 5px;

      .green {
        color: var(--secondary-color);
      }
    }
    .caption {
      font-size: 1.25em;
      font-weight: 600;
      margin-bottom: 20px;
    }
  }
}

.training {
  width: 80%;
  margin: 35px auto 80px auto;

  h2 {
    text-align: center;
  }

  .cards {
    margin-top: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 35px;
  }
}

.how-tos {
  text-align: center;

  .category {
    display: flex;
    gap: 30px;
    font-size: 1.3em;
    justify-content: center;
    margin: 10px 0 20px 0;

    .active {
      height: 5px;
      border-radius: 5px;
      font-weight: 700;
      box-shadow: 0 30px 0 0 var(--secondary-color);
    }
  }

  .articles {
    width: 80%;
    margin: auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    .post {
      max-width: 300px;
      text-align: left;
      padding: 8px;
      border: 1px solid rgba($color: #000000, $alpha: 0.5);
      border-radius: 4px;

      .img {
        height: 160px;
        object-fit: contain;

        img {
          height: inherit;
          object-fit: cover;
          width: 100%;
        }
      }
      .title {
        font-weight: 700;
        font-size: 0.95em;
        margin: 12px 0 12px 0;
      }

      .snippet {
        font-size: 0.9em;
        margin-bottom: 12px;
      }

      .publisher {
        display: flex;
        gap: 10px;
        .author-img {
          height: 50px;
          object-fit: contain;
          border-radius: 50%;

          img {
            height: inherit;
            object-fit: cover;
            width: 100%;
            border-radius: inherit;
          }
        }

        .author {
          display: flex;
          flex-direction: column;
          justify-content: center;

          .name {
            font-size: 0.95em;
            font-weight: 700;
          }
          .date {
            font-size: 0.9em;
          }
        }
      }
    }
  }
}
</style>
