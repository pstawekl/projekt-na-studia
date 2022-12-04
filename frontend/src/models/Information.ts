/* tslint:disable */
/* eslint-disable */
/**
 * Tank Measurement API
 * API for config.json in tank_measurement
 *
 * The version of the OpenAPI document: 0.1.9
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface Information
 */
export interface Information {
    /**
     * 
     * @type {number}
     * @memberof Information
     */
    status: number;
    /**
     * 
     * @type {number}
     * @memberof Information
     */
    affected: number;
    /**
     * 
     * @type {string}
     * @memberof Information
     */
    message: string | null;
}

export function InformationFromJSON(json: any): Information {
    return InformationFromJSONTyped(json, false);
}

export function InformationFromJSONTyped(json: any, ignoreDiscriminator: boolean): Information {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'status': json['status'],
        'affected': json['affected'],
        'message': json['message'],
    };
}

export function InformationToJSON(value?: Information | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'status': value.status,
        'affected': value.affected,
        'message': value.message,
    };
}

