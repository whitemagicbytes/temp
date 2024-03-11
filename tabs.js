import React, { useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs'; // Import from react-tabs
import CommonForm from './CommonForm'; // Assuming CommonForm is in a separate file

interface APIRequestData {
  tabName: string;
  formData: Record<string, string>;
}

const MyTabs = () => {
  const [activeTab, setActiveTab] = useState("tab1");

  const handleFormSubmit = (formData: Record<string, string>) => {
    const apiData: APIRequestData = {
      tabName: activeTab,
      formData,
    };

    // Replace with your actual API call logic
    fetch('/your-api-endpoint', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(apiData),
    })
      .then(response => response.json())
      .then(data => console.log('API response:', data))
      .catch(error => console.error('API call error:', error));
  };

  return (
    <div className="Tabs">
      {/* ... your existing code for tab navigation (if any) */}

      <div className="outlet">
        <Tabs>
          <TabList>
            <Tab onClick={() => setActiveTab('tab1')}>Tab 1</Tab>
            <Tab onClick={() => setActiveTab('tab2')}>Tab 2</Tab>
            <Tab onClick={() => setActiveTab('tab3')}>Tab 3</Tab>
          </TabList>

          <TabPanel>
            <CommonForm activeTab="tab1" onSubmit={handleFormSubmit} />
          </TabPanel>
          <TabPanel>
            <CommonForm activeTab="tab2" onSubmit={handleFormSubmit} />
          </TabPanel>
          <TabPanel>
            <CommonForm activeTab="tab3" onSubmit={handleFormSubmit} />
          </TabPanel>
        </Tabs>
      </div>
    </div>
  );
};

export default MyTabs;
