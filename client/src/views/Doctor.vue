<template>
  <div>
    <div class="big_screen">
      <div class="input_area">
        <label>age_quantile</label>
        <div class="sub_area">
          <input v-model="age_quantile" type="text" placeholder="Please enter">
        </div>
        <label>hemoglobin</label>
        <div class="sub_area">
          <input v-model="hemoglobin" placeholder="Please enter" >
        </div>
        <label>platelets</label>
        <div class="sub_area">
          <input v-model="platelets" placeholder="Please enter" >
        </div>
        <label>MPV</label>
        <div class="sub_area">
          <input v-model="MPV" placeholder="Please enter" >
        </div>
        <label>RBC</label>
        <div class="sub_area">
          <input v-model="RBC" placeholder="Please enter" >
        </div>
        <label>lymphocytes</label>
        <div class="sub_area">
          <input v-model="lymphocytes" placeholder="Please enter" >
        </div>
        <label>MCHC</label>
        <div class="sub_area">
          <input v-model="MCHC" placeholder="Please enter" >
        </div>
        <label>leukocytes</label>
        <div class="sub_area">
          <input v-model="leukocytes" placeholder="Please enter" >
        </div>
        <label>basophils</label>
        <div class="sub_area">
          <input v-model="basophils" placeholder="Please enter" >
        </div>
        <label>MCH</label>
        <div class="sub_area">
          <input v-model="MCH" placeholder="Please enter" >
        </div>
        <label>eosinophils</label>
        <div class="sub_area">
          <input v-model="eosinophils" placeholder="Please enter" >
        </div>
        <label>MCV</label>
        <div class="sub_area">
          <input v-model="MCV" placeholder="Please enter" >
        </div>
        <label>monocytes</label>
        <div class="sub_area">
          <input v-model="monocytes" placeholder="Please enter" >
        </div>
        <label>RDW</label>
        <div class="sub_area">
          <input v-model="RDW" placeholder="Please enter" >
        </div>
        <label>detection_coronaviridae</label>
        <div class="sub_area">
          <input v-model="detection_coronaviridae" placeholder="Please enter" >
        </div>
        <label>detection_orthomyxoviridae</label>
        <div class="sub_area">
          <input v-model="detection_orthomyxoviridae" placeholder="Please enter" >
        </div>
        <label>detection_paramyxoviridae</label>
        <div class="sub_area">
          <input v-model="detection_paramyxoviridae" placeholder="Please enter" >
        </div>
        <label>detection_picornaviridae</label>
        <div class="sub_area">
          <input v-model="detection_picornaviridae" placeholder="Please enter" >
        </div>
        <label>detection_pneumoviridae</label>
        <div class="sub_area">
          <input v-model="detection_pneumoviridae" placeholder="Please enter" >
        </div>
        <a href="javascript:;" class="button1" @click="onsubmit();">Submit</a>
      </div>
      <div class="drag_upload">
        <input type="file" accept=".csv" id = "fileInputCSV" @change="handleChange()"/>
        <div class="result_area">
        <label>Covid-19 Test Result</label>
        </div>
        <input v-model="test_result" placeholder="Please enter" >
        <a href="javascript:" class="button2" @click="submitForUpload();">Upload the
          patient data</a>
        <div class="result_area">
          <label>Query a patient by Private Password</label>
        </div>
        <input v-model="p_index" placeholder="Please enter" >
        <a href="javascript:" class="button3" @click="submitForQuery();">Submit for the query</a>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import detectEthereumProvider from '@metamask/detect-provider';
import Papa from 'papaparse';
// eslint-disable-next-line import/no-cycle
import router from '../router';

export default {
  name: 'Doctor',
  data() {
    return {
      age_quantile: '',
      hemoglobin: '',
      platelets: '',
      MPV: '',
      RBC: '',
      lymphocytes: '',
      MCHC: '',
      leukocytes: '',
      basophils: '',
      MCH: '',
      eosinophils: '',
      MCV: '',
      monocytes: '',
      RDW: '',
      detection_coronaviridae: '',
      detection_orthomyxoviridae: '',
      detection_paramyxoviridae: '',
      detection_picornaviridae: '',
      detection_pneumoviridae: '',
      test_result: '',
      p_index: '',
    };
  },
  methods: {
    predict(val) {
      const path = 'http://localhost:5000/patient';
      axios.post(path, val)
        .then((response) => {
          console.log('Submit Success.');
          const message = `Our AI predict your result is ${response.data.answer}.`;
          alert(message);
          console.log(response.data.answer);
        });
    },
    query(val) {
      const path = 'http://localhost:5000/query';
      axios.post(path, val)
        .then((response) => {
          this.queryBack(response.data.answer);
          console.log(response.data.answer);
          console.log('Query Success.');
        });
    },
    upload(val) {
      const path = 'http://localhost:5000/upload';
      axios.post(path, val)
        .then((response) => {
          const message = `\n Success! \n\n VERY IMPORTANT INFORMATION: \n
          Your private password is ${response.data.password}.\n
          You must remember it and use it to query the record. We will not keep it.\n
          And we will delete it forever.`;
          alert(message);
          console.log(response.data.password);
          console.log('Upload Success.');
        });
    },
    handleChange() {
      const fileInput = document.getElementById('fileInputCSV');
      this.papaParse(fileInput);
    },
    papaParse(obj) {
      console.log(obj);
      let dp;
      Papa.parse(obj.files[0], {
        header: true,
        complete(results) {
          console.log(results);
          dp = results.data;
        },
      });
      setTimeout(() => {
        // console.log(dp);
        this.backInput(dp);
      }, 1500);
      // this.backInput(results);
    },
    backInput(dp) {
      console.log(dp);
      this.age_quantile = dp[0].age_quantile;
      this.hemoglobin = dp[0].hemoglobin;
      this.platelets = dp[0].platelets;
      this.MPV = dp[0].MPV;
      this.RBC = dp[0].RBC;
      this.lymphocytes = dp[0].lymphocytes;
      this.MCHC = dp[0].MCHC;
      this.leukocytes = dp[0].leukocytes;
      this.basophils = dp[0].basophils;
      this.MCH = dp[0].MCH;
      this.eosinophils = dp[0].eosinophils;
      this.MCV = dp[0].MCV;
      this.monocytes = dp[0].monocytes;
      this.RDW = dp[0].RDW;
      this.detection_coronaviridae = dp[0].detection_coronaviridae;
      this.detection_orthomyxoviridae = dp[0].detection_orthomyxoviridae;
      this.detection_paramyxoviridae = dp[0].detection_paramyxoviridae;
      this.detection_picornaviridae = dp[0].detection_picornaviridae;
      this.detection_pneumoviridae = dp[0].detection_pneumoviridae;
    },
    queryBack(dp) {
      console.log(dp);
      // eslint-disable-next-line prefer-destructuring
      this.age_quantile = Number(dp[0]);
      // eslint-disable-next-line prefer-destructuring
      this.test_result = Number(dp[1]);
      // eslint-disable-next-line prefer-destructuring
      this.hemoglobin = dp[2];
      // eslint-disable-next-line prefer-destructuring
      this.platelets = dp[3];
      // eslint-disable-next-line prefer-destructuring
      this.MPV = dp[4];
      // eslint-disable-next-line prefer-destructuring
      this.RBC = dp[5];
      // eslint-disable-next-line prefer-destructuring
      this.lymphocytes = dp[6];
      // eslint-disable-next-line prefer-destructuring
      this.MCHC = dp[7];
      // eslint-disable-next-line prefer-destructuring
      this.leukocytes = dp[8];
      // eslint-disable-next-line prefer-destructuring
      this.basophils = dp[9];
      // eslint-disable-next-line prefer-destructuring
      this.MCH = dp[10];
      // eslint-disable-next-line prefer-destructuring
      this.eosinophils = dp[11];
      // eslint-disable-next-line prefer-destructuring
      this.MCV = dp[12];
      // eslint-disable-next-line prefer-destructuring
      this.monocytes = dp[13];
      // eslint-disable-next-line prefer-destructuring
      this.RDW = dp[14];
      // eslint-disable-next-line prefer-destructuring
      this.detection_coronaviridae = Number(dp[15]);
      // eslint-disable-next-line prefer-destructuring
      this.detection_orthomyxoviridae = Number(dp[16]);
      // eslint-disable-next-line prefer-destructuring
      this.detection_paramyxoviridae = Number(dp[17]);
      // eslint-disable-next-line prefer-destructuring
      this.detection_picornaviridae = Number(dp[18]);
      // eslint-disable-next-line prefer-destructuring
      this.detection_pneumoviridae = Number(dp[19]);
    },
    onsubmit() {
      const data = {
        age_quantile: this.age_quantile,
        hemoglobin: this.hemoglobin,
        platelets: this.platelets,
        MPV: this.MPV,
        RBC: this.RBC,
        lymphocytes: this.lymphocytes,
        MCHC: this.MCHC,
        leukocytes: this.leukocytes,
        basophils: this.basophils,
        MCH: this.MCH,
        eosinophils: this.eosinophils,
        MCV: this.MCV,
        monocytes: this.monocytes,
        RDW: this.RDW,
        detection_coronaviridae: this.detection_coronaviridae,
        detection_orthomyxoviridae: this.detection_orthomyxoviridae,
        detection_paramyxoviridae: this.detection_paramyxoviridae,
        detection_picornaviridae: this.detection_picornaviridae,
        detection_pneumoviridae: this.detection_pneumoviridae,
      };
      this.predict(data);
    },
    submitForQuery() {
      this.query(this.p_index);
    },
    submitForUpload() {
      const data = {
        age_quantile: this.age_quantile,
        test_result: this.test_result,
        hemoglobin: this.hemoglobin,
        platelets: this.platelets,
        MPV: this.MPV,
        RBC: this.RBC,
        lymphocytes: this.lymphocytes,
        MCHC: this.MCHC,
        leukocytes: this.leukocytes,
        basophils: this.basophils,
        MCH: this.MCH,
        eosinophils: this.eosinophils,
        MCV: this.MCV,
        monocytes: this.monocytes,
        RDW: this.RDW,
        detection_coronaviridae: this.detection_coronaviridae,
        detection_orthomyxoviridae: this.detection_orthomyxoviridae,
        detection_paramyxoviridae: this.detection_paramyxoviridae,
        detection_picornaviridae: this.detection_picornaviridae,
        detection_pneumoviridae: this.detection_pneumoviridae,
      };
      this.upload(data);
    },
  },
  async mounted() {
    const provider = await detectEthereumProvider();
    if (provider === window.ethereum) {
      window.ethereum.enable().then(() => {
      });
    } else {
      console.log(provider);
      alert('Please use MetaMask');
    }
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const currentAccounts = accounts[0];
    console.log(currentAccounts);
    if (currentAccounts !== '0xb7248a0173d8d7b1c9cf5735460ce42ce6f12ffc') {
      alert('Please use a doctor account!');
      setTimeout(() => {
        router.replace({ path: 'patient' });
      }, 300);
    }
    window.ethereum.on('accountsChanged', (accounts1) => {
      // Time to reload your interface with accounts[0]!\
      console.log(accounts1[0]);
      if (accounts1[0] !== '0xb7248a0173d8d7b1c9cf5735460ce42ce6f12ffc') {
        alert('Please use a doctor account!');
        setTimeout(() => {
          router.replace({ path: 'patient' });
        }, 300);
      }
    });
  },
};
</script>

<style scoped>

.input_area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.sub_area {
  margin-bottom: 0.5em;
}
.big_screen {
  display: flex;
  justify-content: center;
}
.drag_upload {
  display: flex;
  flex-direction: column;
  margin-top: 2em;
  margin-left: 2em;
}
.result_area {
  margin-top: 3em;
}
.button2 {
  margin-top: 0.5em;
}
.button3 {
  margin-top: 0.5em;
}
</style>
