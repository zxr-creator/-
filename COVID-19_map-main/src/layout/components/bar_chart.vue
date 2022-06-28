<template>
  <div id="bar_chart" style="height: 100%; width: 100%"></div>
</template>

<script>
import * as echarts from "echarts"


export default {
  name: 'Barchart',
  data() {
    return {
    }
  },
  mounted() {
    this.drawChart();
  },

  methods: {

    drawChart() {

      let bar_chart=echarts.init(document.getElementById("bar_chart"));
      setTimeout(() =>{
      bar_chart.setOption({
        title: {
          text: '疫情前后豆瓣每年各类型电影情感分析',
          textStyle:{
                color:'#8ec06c',
                frotSize:'40'
              }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          left:'7%',
          top:"8%"
        },
        grid: {
          left: '3%',
          right: '4%',
          top:"20%",
          bottom:"0%",
          containLabel: true
        },
        xAxis: {
          type: 'value',
          boundaryGap: [0, 0.00001],
          // 字体设置
          axisLabel:{
            type:"solid",
            color:"#f48924",
            fontSize:"14",
            nameLocation:'end'
            },
          // 坐标轴颜色
          axisLine:{
            color:'#56a0d3'
          }
        },
        yAxis: {
          type: 'category',
          data: ['剧情','喜剧','动作','爱情','科幻','动画','悬疑','恐怖'],
          // 字体设置
          axisLabel:{
            type:"solid",
            color:"#a626aa",
            fontSize:"12",
            nameLocation:'end'
            },
          // 坐标轴颜色
          axisLine:{
            color:'#56a0d3'
          }
        },
        series: [
          {
            name: '2018',
            type: 'bar',
            data: [
              0.76,
              0.83,
              0.92,
              0.66,
              0.87,
              0.91,
              0.68,
              0.87
            ]
          },
          {
            name: '2019',
            type: 'bar',
            data: [
              0.64,
              0.78,
              0.91,
              0.84,
              0.75,
              0.56,
              0.61,
              0.53
            ]
          },
          {
            name: '2020',
            type: 'bar',
            data: [

              0.53,
              0.82,
              0.66,
              0.68,
              0.63,
              0.76,
              0.53,
              0.77

            ]
          },
          {
            name: '2021',
            type: 'bar',
            data: [

              0.56,
              0.88,
              0.63,
              0.78,
              0.71,
              0.75,
              0.59,
              0.69

            ]
          },
          {
            name: '2022',
            type: 'bar',
            data: [

              0.52,
              0.84,
              0.66,
              0.75,
              0.51,
              0.79,
              0.70,
              0.72
            ]
          },
        ]
      })
      },20)

    },

  },

};
</script>

<style scoped>

</style>
