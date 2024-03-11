import React from 'react';
import { useForm } from 'react-hook-form';

interface FieldDefinition {
  regex?: RegExp;
  placeholder?: string;
}

interface Props {
  activeTab: string;
  onSubmit: (formData: Record<string, string>) => void;
}

function CommonForm({ activeTab, onSubmit }: Props) {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const fieldDefinitions: Record<string, FieldDefinition> = {
    a: {
      regex: /^[a-zA-Z]+$/,
      placeholder: 'Enter text only (a-z, A-Z)',
    },
    b: {
      regex: /^\d{3}-\d{2}-\d{4}$/,
      placeholder: 'Enter in format XXX-XX-XXXX (b)',
    },
    c: {
      regex: /^.+@.+\..+$/,
      placeholder: 'Enter a valid email address (c)',
    },
    // Add similar definitions for fields d and e
    d: {
      regex: /^[0-9]+$/,
      placeholder: 'Enter only numbers (d)',
    },
    e: {
      regex: /^(http|https):\/\/[^\s]+/,
      placeholder: 'Enter a valid URL (e)',
    },
  };

  const fieldsByTab: Record<string, string[]> = {
    tab1: ['a', 'b', 'c', 'd', 'e'],
    tab2: ['a', 'b', 'c', 'd', 'f', 'g'],
    tab3: ['a', 'b', 'c', 'd', 'f', 'i'],
  };

  const activeFields = fieldsByTab[activeTab] || [];

  // Extract form data based on active fields
  const getFormData = (data: Record<string, unknown>) => {
    const formData: Record<string, string> = {};
    activeFields.forEach((field) => {
      formData[field] = String(data[field]); // Type casting to string
    });
    return formData;
  };

  return (
    <form onSubmit={handleSubmit(() => onSubmit(getFormData(register('myForm'))))}>
      {activeFields.map((field) => (
        <div key={field}>
          <label htmlFor={field}>{field}</label>
          <input
            type="text"
            id={field}
            {...register(`myForm.${field}`, { // Register each field with a unique name
              required: true,
              pattern: fieldDefinitions[field]?.regex,
            })}
            placeholder={fieldDefinitions[field]?.placeholder}
          />
        </div>
      ))}
      <button type="submit">Submit {activeTab}</button>
    </form>
  );
}

export default CommonForm;
