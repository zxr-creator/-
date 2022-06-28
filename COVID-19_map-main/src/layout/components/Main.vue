<template>
  <!-- ---MAIN--- -->
  <section class="mainbox">
    <!-- ---LEFT BOX--- -->
    <div class="column1">
      <!-- MAP BOX -->
      <div class="panel-map">
        <Map/>
      </div>
      <div class="panel-graph1">
        <Scene1/>  
      </div>
    </div> 
    <!-- ---RIGHT BOX--- -->
    <div class="column">
      <div class="panel1">
        <ScatterChart/>
      </div>
      <div class="panel2">
        <div class="panel2_1">
          <Scene3bar/>
        </div>
        <div class="panel2_2">
          <PieChart/>
        </div>
      </div>
      <div class="panel3">
        <div class="panel3_1">
          <Linerace/>
        </div>
        <div class="panel3_2">
          <Barchart/>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Map from '@/views/map/index'
import Scene1 from '@/layout/components/HelloWorld'
import Scene3bar from '@/layout/components/BarChart'
import PieChart from '@/layout/components/PieChart'
import ScatterChart from '@/layout/components/ScatterChart'
import Linerace from '@/layout/components/line_race_chart'
import Barchart from '@/layout/components/bar_chart'

export default {
  name: "Main",
  components: {
    Map,
    Scene1,
    Scene3bar,
    PieChart,
    ScatterChart,
    Linerace,
    Barchart
  }
}
</script>

<style scoped>

</style>
