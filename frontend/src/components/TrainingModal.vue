<script setup>
import { reactive } from 'vue'
import Button from '../components/DynamicButton.vue'
import { Icon } from '@iconify/vue'

const levels = reactive([
  { id: 1, skill: 'Beginner', active: false },
  { id: 2, skill: 'Intermediate', active: false },
  { id: 3, skill: 'Advanced', active: false }
])

const skills = reactive([
  { id: 1, trait: 'Shooting', active: false, icon: 'icon-park-outline:basketball-one' },
  { id: 2, trait: 'Dribbling', active: false, icon: 'tabler:play-basketball' },
  { id: 3, trait: 'Passing', active: false, icon: 'ph:basketball' },
  { id: 4, trait: 'Finishing', active: false, icon: 'icon-park-outline:play-basketball' }
])


function getSelection(){
  let skill = ""
  let area = ""

  for (const item of levels) {
    if (item.active == true) {
      skill = item.skill
    }
  }

  for (const item of skills) {
    if (item.active == true) {
      area = item.trait
    }
  }

  return `/trainings/${skill}+${area}+drills`
}



//selects item and deselects others
function toggleActive(array, id) {
  let arr = eval(array) //array holds name of array(ie levels, skills)

  //turn off other selections
  for (const item of arr) {
    if (item.id == id) continue // do not turn off active selection
    item.active = false
  }

  id = id - 1 //index is n-1
  arr[id].active = !arr[id].active //invert value of active selection
}

//clear selections
function clear() {
  for (const item of levels) item.active = false //clear selections for level
  for (const item of skills) item.active = false //clear selections for skills
}
</script>

<template>
  <div class="background">
    <div class="popup">
      <Icon @click="$emit('closeModal')" icon="iconamoon:close-bold" class="close-btn" />

      <div class="heading">
        <h2>Personalize Training</h2>
        <p>Choose skill level and area you wish to improve on</p>
      </div>

      <h3>Skill Level</h3>
      <div class="items">
        <div
          :class="{ skill: true, active: level.active }"
          v-for="level in levels"
          :key="level.id"
          @click="toggleActive('levels', level.id)"
        >
          <div class="text">{{ level.skill }}</div>
          <div class="icons">
            <Icon icon="material-symbols:star" v-for="icon in level.id" :key="icon" />
          </div>
        </div>
      </div>

      <h3>Area of Focus</h3>
      <div class="items">
        <div
          :class="{ skill: true, active: skill.active }"
          v-for="skill in skills"
          :key="skill.id"
          @click="toggleActive('skills', skill.id)"
        >
          <div class="text">{{ skill.trait }}</div>
          <div class="icon"><Icon :icon="skill.icon" /></div>
        </div>
      </div>

      <div class="buttons">
        <Button @click="$emit('closeModal')" :route="getSelection()">Get Training</Button>
        <Button type="danger" @click="clear()">Clear Selection</Button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.background {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background: rgba($color: #000000, $alpha: 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow-y: auto;

  .popup {
    position: relative;
    background: #fff;
    padding: 30px;
    max-width: 95%;
    border-radius: 4px;

    .close-btn {
      position: absolute;
      top: 12px;
      right: 12px;
      font-size: 1.6em;
      cursor: pointer;
    }
    .heading {
      margin-bottom: 30px;
    }

    .buttons {
      display: flex;
      gap: 12px;
    }

    h3 {
      margin-bottom: 4px;
    }

    .items {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      margin-bottom: 25px;

      .skill {
        border: 0.5px solid var(--secondary-color);
        padding: 8px 16px;
        border-radius: 4px;
        cursor: pointer;
        .text {
          font-weight: 500;
          text-align: center;
          margin-bottom: 5px;
        }

        .icons {
          display: flex;
          gap: 3px;
          justify-content: center;
          font-size: 1.4em;
          color: var(--secondary-color);
        }

        .icon {
          display: flex;
          justify-content: center;
          font-size: 2.5em;
        }
      }

      .skill.active {
        background: var(--secondary-color);
        border: 2px solid #000;

        .text {
          font-weight: 700;
        }

        .icons {
          color: #000;
        }
      }
    }
  }
}
</style>
